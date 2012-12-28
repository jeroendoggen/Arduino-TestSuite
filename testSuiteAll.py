#!/usr/bin/env python
#
# Arduino TestSuite to automate unit tests on the Arduino platform
# Copyright (C) 2012  Jeroen Doggen <jeroendoggen@gmail.com>
#
# Version History:
#  - Version 0.1: call scons
#                 run unit test
#                 print summary
#                 
#  - Version 0.2: subprocess for arscons
#                 classes: Test, TestSuite, InfoPrinter, 
#
# Roadmap:
#  - Clean up code
#  - use subprocesses
#  - accept commandline parameters (options, silent, debug,..)
#  - logging to a file
#  - what to to when arscons fails? (how to report?)
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

DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUDRATE = 9600
ser = ""

librariesPath = "/usr/share/arduino/libraries"


def initSerialPort():
    global ser
    ser = serial.Serial(DEFAULT_PORT, DEFAULT_BAUDRATE)
    ser.flush()

class Helper:
    def timeout_command(self, command, timeout):
        #"""call shell-command and either return its output or kill it
        #if it doesn't normally exit within timeout seconds and return None"""
        import subprocess, datetime, os, time, signal

        cmd = command.split(" ")
        start = datetime.datetime.now()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, \
          stderr=subprocess.PIPE)

        while process.poll() is None:
            time.sleep(1)
            now = datetime.datetime.now()
            if (now - start).seconds > timeout:
                os.kill(process.pid, signal.SIGKILL)
                os.waitpid(-1, os.WNOHANG)
                return None

        return process.poll()

class InfoPrinter:
    def printMarker1(self):
        print ('===================================================================')

    def printMarker2(self):
        print ('-------------------------------------------------------------------')

    def printProgramFlow(self):
        print ('')
        print ('Program flow: ')
        print (' 1. Compile TestSuite sketch')
        print (' 2. Upload sketch using Arscons')
        print (' 3. Check unit test output')

    def printTop(self):
        print ('')
        printer.printMarker1()
        print ('Planned tests:')
        
    def printSetupInfo(self, item):
        print ('')
        printer.printMarker1()
        print ('Starting test: ' + item )
        printer.printMarker2()
        print ('Uploading sketch to Arduino...')


class TestSuite:
    notFinished = True    # boolean value
    uploadFinished = False
    FailedTestList = []
    PassedTestList = []
    failureCount= 0
    line = []
    ser
        
    def printPlannedTests(self):
        printer.printTop()
        for index, item in enumerate(testList):
            print (item.path)
        printer.printProgramFlow()

    
    def runTests(self):
        for index, item in enumerate(testList):
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
            self.failureCount = self.failureCount+1
            
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
            return True
        else:
            return False
        
    #def debug(self):


class Test:
    def __init__(self, path):
        self.path = path

suite = TestSuite()
printer = InfoPrinter()
helper = Helper()

distanceTest= Test("DistanceSensor/examples/GP2Y0A21YK/TestSuite/")
moduleTest= Test("LT_Module/examples/TestSuite/")

testList = [distanceTest, moduleTest ]

def main(argv=None):
    initSerialPort()
    #suite.debug()
    suite.printPlannedTests()
    suite.runTests()
    suite.printSummary()
    #suite.report()


if __name__ == "__main__":
    sys.exit(main())
