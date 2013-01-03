#!/usr/bin/env python
#
# Arduino TestSuite to automate unit tests on the Arduino platform
# Copyright (C) 2012  Jeroen Doggen <jeroendoggen@gmail.com>
# More info in "main.py"
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.
from __future__ import print_function, division  # We require Python 2.6+

import os
import time
import argparse
import datetime

import infoprinter
from arduino_testsuite.testhelper import TestHelper
from arduino_testsuite.settings import Settings


scriptPath = os.getcwd()


helper = TestHelper()


class TestSuite:
    notFinished = True    # boolean value
    foundTestPath = False
    uploadStatus = False
    FailedTestList = []
    PassedTestList = []
    failureCount = 0
    line = []
    testList = []
    config = Settings()

    def __init__(self):
        """Initialize the suite: cli, config file, serial port."""
        self.config.getCliArguments()
        self.testList = self.config.readConfigfile()
        self.ser = self.config.initSerialPort()

    def printPlannedTests(self):
        """Print an overview of all the test that are planned"""
        infoprinter.planned_tests(self.testList)
        infoprinter.programflow()

    def runTests(self, timeout):
        """Run all the tests"""
        for index, currentTest in enumerate(self.testList):
            self.goToTestPath(currentTest)
            if (self.foundTestPath):
                self.foundTestPath = False
                print("Starting upload...")
                self.uploadSketch(timeout)
                if (self.uploadStatus == 0):
                    print("Start tests...")
                    self.analyzeOutput(timeout, currentTest)
                else:
                    self.addToFailedList(currentTest)

    def goToTestPath(self, currentTest):
        """Go to the folder of the current test"""
        infoprinter.setup_info(currentTest)
        try:
            os.chdir(scriptPath)
        except OSError:
            print("Error: unable to open the script folder")
            print("This should never happen...")
        try:
            os.chdir(currentTest)
            self.foundTestPath = True
        except OSError:
            print("Error: unable to open test folder")
            print("Check your config file")
            self.foundTestPath = False
            self.addToFailedList(currentTest)

    def uploadSketch(self, timeout):
        """Upload the sketch to the Arduino board"""
        self.uploadStatus = helper.timeout_command("scons upload", timeout)
        infoprinter.upload_status(self.uploadStatus)

    def analyzeOutput(self, timeout, currentTest):
        """Analyze the test output that is received over the serial port"""
        start = datetime.datetime.now()
        while self.notFinished:
            self.readLine(currentTest)
            time.sleep(0.1)
            now = datetime.datetime.now()
            if (now - start).seconds > timeout:
                print ("Test timeout after ", end="")
                print (timeout, end="")
                print (" seconds")
                self.notFinished = False
        self.notFinished = True   # to allow the next test to start
        if (self.line[11] == self.line[25]):
            if currentTest not in self.FailedTestList:
                self.addToPassedList(currentTest)
        else:
            self.FailedTestList.append(currentTest)
            self.failureCount = self.failureCount + 1

    def readLine(self, currentTest):
        """Read one line of text over the serial port"""
        try:
            self.line = self.ser.readline().decode('utf-8')[:-1]
            print (self.line)
        except:
            print ("unexpectedly lost serial connection")
            self.addToFailedList(currentTest)
        if(self.line.find("Tests run:") == 0):
            self.notFinished = False

    def printSummary(self):
        """Print the summary of all the tests."""
        infoprinter.summary(self.FailedTestList, self.PassedTestList)

    def exitValue(self):
        """Generate the exit value for the application."""
        return(helper.exitValue(self.failureCount))

    def addToFailedList(self, currentTest):
        """Add the current test to the list of failed tests."""
        self.FailedTestList.append(currentTest)

    def addToPassedList(self, currentTest):
        """Add the current test to the list of passed tests."""
        self.PassedTestList.append(currentTest)
