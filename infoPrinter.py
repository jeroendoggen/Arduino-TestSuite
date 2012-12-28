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


class InfoPrinter:
    def printMarker1(self):
        print ('=============================================================')

    def printMarker2(self):
        print ('-------------------------------------------------------------')

    def printProgramFlow(self):
        print ('')
        print ('Program flow: ')
        print (' 1. Compile TestSuite sketch')
        print (' 2. Upload sketch using Arscons')
        print (' 3. Check unit test output')

    def printTop(self):
        print ('')
        self.printMarker1()
        print ('Planned tests:')

    def printSetupInfo(self, item):
        print ('')
        self.printMarker1()
        print ('Starting test: ' + item)
        self.printMarker2()
        print ('Uploading sketch to Arduino...')
