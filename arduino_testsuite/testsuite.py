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

from arduino_testsuite.infoprinter import InfoPrinter
from arduino_testsuite.testhelper import TestHelper
from arduino_testsuite.settings import Settings


scriptPath = os.getcwd()

printer = InfoPrinter()
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
        self.config.getCliArguments()
        self.testList = self.config.readConfigfile()

    def printPlannedTests(self):
        printer.plannedTests(self.testList)

    def runTests(self, timeout):
        for index, currentTest in enumerate(self.testList):
            self.setUp(currentTest)
            if (self.foundTestPath):
                self.foundTestPath = False
                print("Starting upload...")
                self.uploadSketch(timeout)
                if (self.uploadStatus == 0):
                    print("Start tests...")
                    self.analyzeOutput(timeout, currentTest)
                else:
                    self.addToFailedList(currentTest)

    def setUp(self, currentTest):
        printer.printSetupInfo(currentTest)
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
        sconsCommand = "scons"
        if self.config.isWindows():
            sconsCommand += ".bat"
        sconstructDirArgument = "--directory=" + os.getcwd()
        portArgument = "ARDUINO_PORT=" + self.config.serialPort
        boardArgument = "ARDUINO_BOARD=" + self.config.board
        self.uploadStatus = helper.timeout_command(sconsCommand + " " + sconstructDirArgument + " " + boardArgument + " " + portArgument + " upload", timeout)
        printer.uploadStatus(self.uploadStatus)

    def analyzeOutput(self, timeout, currentTest):
        self.ser = self.config.initSerialPort()

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

        self.ser.close()

    def readLine(self, currentTest):
        try:
            self.line = self.ser.readline().decode('utf-8')[:-1]
            print (self.line)
        except:
            print ("unexpectedly lost serial connection")
            self.addToFailedList(currentTest)
        if(self.line.find("Tests run:") == 0):
            self.notFinished = False

    def printSummary(self):
        printer.printSummary(self.FailedTestList, self.PassedTestList)

    def report(self):
        return(helper.report(self.failureCount))

    def addToFailedList(self, currentTest):
        self.FailedTestList.append(currentTest)

    def addToPassedList(self, currentTest):
        self.PassedTestList.append(currentTest)
