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


class InfoPrinterHelper:
    def printMarker1(self):
        print ("=============================================================")

    def printMarker2(self):
        print ("-------------------------------------------------------------")

    def printTop(self):
        print ("")
        self.printMarker1()
        print ("Planned tests:")

    def printProgramFlow(self):
        print ("")
        print ("Program flow: ")
        print (" 1. Compile TestSuite sketch")
        print (" 2. Upload sketch using Arscons")
        print (" 3. Check unit test output")


class InfoPrinter:
    helper = InfoPrinterHelper()

    def plannedTests(self, testList):
        self.helper.printTop()
        for index, item in enumerate(testList):
            print (" ", end="")
            print (index + 1, end="")
            print (". ", end="")
            print (item)
        self.helper.printProgramFlow()

    def printSetupInfo(self, item):
        print ("")
        self.helper.printMarker1()
        print ("Starting test: " + item)
        self.helper.printMarker2()
        print ("Compiling & uploading sketch to Arduino...")

    def printSummary(self, FailedTestList, PassedTestList):
        print ("")
        self.helper.printMarker1()
        print ("Summary: ")
        self.helper.printMarker2()
        print ("Failed tests:")
        for index, item in enumerate(FailedTestList):
            print (" " + str(index + 1) + "." + item)
        print ("")
        print ("Passed tests:")
        for index, item in enumerate(PassedTestList):
            print (" " + str(index + 1) + "." + item)
        self.helper.printMarker1()
        print ("")

    def uploadStatus(self, uploadStatus):
        if (uploadStatus == 0):
            self.uploadFinished = True
            print ("Upload succesfull")
            #print(".", end="")
        else:
            self.uploadFinished = False
            print ("Upload Failed")
