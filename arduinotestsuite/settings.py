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

#platform = os.environ.get('PLATFORM')

#if platform == 'darwin':
    ## For MacOS X, pick up the AVR tools from within Arduino.app
    #ARDUINO_HOME_DEFAULT = '/Applications/Arduino.app/Contents/Resources/Java'
    #ARDUINO_PORT_DEFAULT = getUsbTty('/dev/tty.usbserial*')
    #SKETCHBOOK_HOME_DEFAULT = ''
#elif platform == 'win32':
    ## For Windows, use environment variables.
    #ARDUINO_HOME_DEFAULT = os.environ.get('ARDUINO_HOME')
    #ARDUINO_PORT_DEFAULT = os.environ.get('ARDUINO_PORT')
    #SKETCHBOOK_HOME_DEFAULT = ''
#else:
    ## For Ubuntu Linux (9.10 or higher)
    #ARDUINO_HOME_DEFAULT = '/usr/share/arduino/'
    #ARDUINO_PORT_DEFAULT = getUsbTty('/dev/ttyUSB*')
    #AVR_BIN_PREFIX = 'avr-'
    #SKETCHBOOK_HOME_DEFAULT = os.path.realpath('~/share/arduino/sketchbook/')


class Settings:
    DEFAULT_PORT = "/dev/ttyUSB0"
    DEFAULT_BAUDRATE = 9600
    DEFAULT_CONFIGFILE = "planned-tests.conf"
    serialPort = DEFAULT_PORT
    baudrate = DEFAULT_BAUDRATE
    configFile = DEFAULT_CONFIGFILE

    def getCliArguments(self):
# This needs to be indented like this to print it correctly on the cli
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Arduino TestSuite commandline parameters:\
 serial port, inputfile',
            epilog=textwrap.dedent('''\
This should be enough information to explain how you can call this script
Report bugs to jeroendoggen@gmail.com.'''))
        parser.add_argument('-p', metavar='port',
          help='The name of the serial port')
        parser.add_argument('-f', metavar='file',
          help='The inputfile containing the requested tests')
        parser.add_argument('-b', metavar='baudrate',
          help='The baudrate of the serial port')
        args = parser.parse_args()
        if (args.p is not None):
            self.serialPort = args.p
        if (args.f is not None):
            self.configFile = args.f
        if (args.b is not None):
            self.baudrate = args.b

    def initSerialPort(self):
        ser = serial.Serial(self.serialPort, self.baudrate)
        ser.flush()
        return(ser)

    def readConfigfile(self):
        with open(self.configFile, 'r') as f:
            testList = f.read().splitlines()
        return testList
