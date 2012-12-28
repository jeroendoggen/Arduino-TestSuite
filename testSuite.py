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

import sys
import serial
import time
import os
import subprocess

from infoPrinter import InfoPrinter
from testHelper import TestHelper

DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUDRATE = 9600
ser = ""

librariesPath = "/usr/share/arduino/libraries"

printer = InfoPrinter()
helper = TestHelper()


def initSerialPort():
    global ser
    ser = serial.Serial(DEFAULT_PORT, DEFAULT_BAUDRATE)
    ser.flush()


class TestSuite:
    notFinished = True    # boolean value
    uploadFinished = False
    FailedTestList = []
    PassedTestList = []
    failureCount = 0
    line = []
    testList = []

    def __init__(self, testList):
        self.testList = testList
        initSerialPort()

    def printPlannedTests(self):
        printer.printTop()
        for index, item in enumerate(self.testList):
            print (item.path)
        printer.printProgramFlow()

    def runTests(self):
        for index, item in enumerate(self.testList):
            print (item.path)
            self.setUp(item.path)
            self.uploadSketch()
            self.analyzeOutput(item.path)

    def setUp(self, item):
        os.chdir(librariesPath)
        os.chdir(item)
        printer.printSetupInfo(item)

    def uploadSketch(self):
        state = helper.timeout_command("scons upload", 10)
        if (state == 0):
            self.uploadFinished = True
            print ('Upload succesfull')
            #print('.', end="")
        else:
            self.uploadFinished = False
            print ('Upload Failed')

    def analyzeOutput(self, item):
        while self.notFinished:
            self.readLine()
            time.sleep(0.1)
        self.notFinished = True   # to allow the next test to start
        if (self.line[11] == self.line[25]):
            self.PassedTestList.append(item)
        else:
            self.FailedTestList.append(item)
            self.failureCount = self.failureCount + 1

    def readLine(self):
        try:
            self.line = ser.readline().decode('utf-8')[:-1]
            print (self.line)
        except:
            print ('unexpectedly lost serial connection')
        if(self.line.find("Tests run:") == 0):
            self.notFinished = False

    def printSummary(self):
        print ('')
        printer.printMarker1()
        print ('Summary: ')
        printer.printMarker2()
        print ('Failed tests:')
        for index, item in enumerate(self.FailedTestList):
            print (' ' + str(index + 1) + '.' + item)
        print ('')
        print ('Passed tests:')
        for index, item in enumerate(self.PassedTestList):
            print (' ' + str(index + 1) + '.' + item)
        printer.printMarker1()
        print ('')

    def report(self):
        if (self.failureCount == 0):
            return 0
        else:
            return 42
