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
#                 classes: Test, TestSuite, InfoPrinter
#                 Divided the code in several modules
#
# Roadmap:
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


from test import Test
from testSuite import TestSuite

DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUDRATE = 9600
ser = ""

librariesPath = "/usr/share/arduino/libraries"

distanceTest= Test("DistanceSensor/examples/GP2Y0A21YK/TestSuite/")
moduleTest= Test("LT_Module/examples/TestSuite/")

testList = [distanceTest, moduleTest ]

suite = TestSuite(testList)



def main(argv=None):
    suite.printPlannedTests()
    suite.runTests()
    suite.printSummary()
    #suite.report()


if __name__ == "__main__":
    sys.exit(main())
