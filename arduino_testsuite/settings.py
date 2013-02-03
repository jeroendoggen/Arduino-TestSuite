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

import argparse
import serial
import textwrap
import sys
import platform

class Settings:
    DEFAULT_PORT_UNIX = "/dev/ttyUSB0"
    DEFAULT_PORT_WINDOWS = "COM3"
    DEFAULT_BOARD = "atmega328"
    DEFAULT_BAUDRATE = 9600
    DEFAULT_CONFIGFILE = "planned-tests.conf"
    board = DEFAULT_BOARD
    baudrate = DEFAULT_BAUDRATE
    configFile = DEFAULT_CONFIGFILE

    def __init__(self):
        self.serialPort = self.defaultPort()

    def getCliArguments(self):
# This needs to be indented like this to print it correctly on the cli
        parser = argparse.ArgumentParser(
            prog='arduino_testsuite',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Arduino TestSuite commandline arguments:',
            epilog=textwrap.dedent('''\

Report bugs to jeroendoggen@gmail.com.'''))
        parser.add_argument('-p', metavar='port',
          help='Set the name of the serial port')
        parser.add_argument('-d', metavar='board',
          help='Set the name of the board as defined in boards.txt')
        parser.add_argument('-f', metavar='file',
          help='Select the inputfile containing the requested tests')
        parser.add_argument('-b', metavar='baudrate',
          help='Set the baudrate of the serial port')
        args = parser.parse_args()
        if (args.p is not None):
            self.serialPort = args.p
        if (args.d is not None):
            self.board = args.d
        if (args.f is not None):
            self.configFile = args.f
        if (args.b is not None):
            self.baudrate = args.b

    def initSerialPort(self):
        ser = serial.Serial(self.serialPort, self.baudrate)
        ser.flush()
        return(ser)

    def readConfigfile(self):
        testList = []
        try:
            with open(self.configFile, 'r') as f:
                testList = f.read().splitlines()
        except IOError:
            print ("Error: 'planned-tests.conf' not found!")
            print ("Aborting test session.")
            sys.exit(1)
        return testList

    def defaultPort(self):
        if self.isWindows():
            return self.DEFAULT_PORT_WINDOWS

        return self.DEFAULT_PORT_UNIX

    def isWindows(self):
        return platform.system() == 'Windows'
