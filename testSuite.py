#!/usr/bin/env python
#
# Arduino TestSuite to automate unit tests on the Arduino platform
# Copyright (C) 2012  Jeroen Doggen <jeroendoggen@gmail.com>
#
# Version History:
#  - Version 0.1: call scons, run unit test, print summary
#
# Roadmap:
#  - Clean up code
#  - use subprocesses
#  - accept commandline parameters (options, silent, debug,..)
#  - logging to a file
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys,serial,time,os

DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUDRATE = 9600

scriptPath = os.getcwd()

ser = serial.Serial(DEFAULT_PORT, DEFAULT_BAUDRATE)
ser.flush()

notFinished = True    # boolean value
line = ""

TestList = [ "DistanceSensor/examples/GP2Y0A21YK/TestSuite/",
             "LT_Module/examples/TestSuite/" ]
             
FailedTestList = []
PassedTestList = []

def printMarker1():
    print "================================================================================"
    
def printMarker2():
    print "--------------------------------------------------------------------------------"    

def readLine():
    global line,notFinished
    line = ser.readline()
    line = line[:-1]
    print line
    if( line.find("Tests run:") == 0 ):
        notFinished = False
     
def printPlannedTests():
    print ""
    printMarker1()
    print "Planned tests:"
    for index, item in enumerate(TestList):
        print " " + str(index+1) + ". " + item
    print ""  
    print "Program flow: "  
    print " 1. Compile TestSuite sketch"
    print " 2. Upload sketch using Arscons"
    print " 3. Check unit test output"
    print ""  
    
def printSummary():
    printMarker1()
    print "Summary: " 
    print "Failed tests:"
    for index, item in enumerate(FailedTestList):
        print " " + str(index+1) + ". " + item
    print ""  
    print "Passed tests:"
    for index, item in enumerate(PassedTestList):
        print " " + str(index+1) + ". " + item
    printMarker1()
    print ""

def uploadSketch():
    os.system("scons upload >> /dev/null")

def analyzeOutput(item):
    global notFinished,PassedTestList
    printMarker2()
    while notFinished:
        readLine()
        time.sleep(0.000001)
    notFinished = True   # to allow the next test to start
    if (line[11] == line[25]):
        PassedTestList.append(item)
    else:
        FailedTestList.append(item)
    
def startTests():
    for index, item in enumerate(TestList):
        os.chdir(scriptPath)
        os.chdir(item)
        printMarker1()
        print ""
        print "Starting test: " + item
        printMarker2()
        uploadSketch()
        analyzeOutput(item)
              
def main(argv=None): 
    printPlannedTests()
    startTests()
    printSummary()
    
if __name__ == "__main__":
    sys.exit(main())
    