""" arduino_testsuite: Settings class

get the cli arguments
setup the serial port
read the config file

"""

from __future__ import print_function, division  # We require Python 2.6+

import argparse
import sys
import logging
import platform

try:
    import serial
except ImportError as exc:
    print("Error: failed to import pyserial module")
    print("Solution: you probably need to install the pyserial module")
    sys.exit(0)

logging.basicConfig(filename='example.log',
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(message)s")
LOGGER = logging.getLogger(__name__)


class Settings:
    """Configure the settings of the program"""
    DEFAULT_PORT_UNIX = "/dev/ttyUSB0"
    DEFAULT_PORT_WINDOWS = "COM3"
    DEFAULT_BOARD = "atmega328"
    DEFAULT_BAUDRATE = 9600
    DEFAULT_CONFIGFILE = "planned-tests.conf"
    board = DEFAULT_BOARD
    baudrate = DEFAULT_BAUDRATE
    config_file = DEFAULT_CONFIGFILE

    def __init__(self):
        """Initialize the platform-specific serial port"""
        self.serial_port = self.default_port()

    def get_cli_arguments(self):
        """Read all the cli arguments."""
        """This needs to be indented like this to print it correctly on cli"""
        parser = argparse.ArgumentParser(
            prog="arduino_testsuite",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Arduino TestSuite commandline arguments:",
            epilog="Report bugs to jeroendoggen@gmail.com.")
        parser.add_argument("-p", metavar="port",
          help="Set the name of the serial port")
        parser.add_argument('-d', metavar='board',
          help='Set the name of the board as defined in boards.txt')
        parser.add_argument("-f", metavar="file",
          help="Select the inputfile containing the requested tests")
        parser.add_argument("-b", metavar="baudrate",
          help="Set the baudrate of the serial port")
        args = parser.parse_args()
        if (args.p is not None):
            self.serial_port = args.p
        if (args.d is not None):
            self.board = args.d
        if (args.f is not None):
            self.config_file = args.f
        if (args.b is not None):
            self.baudrate = args.b

    def init_serial_port(self):
        """Initialize the serial port."""
        try:
            ser = serial.Serial(self.serial_port, self.baudrate)
            ser.flush()
        except IOError:
            LOGGER.warning("Unable to connect to serial port")
            print("Unable to connect to serial port: ", end="")
            print(self.serial_port)
            sys.exit(1)
        return(ser)

    def read_testlist_file(self):
        """Read the config file to get the testlist."""
        test_list = []
        try:
            with open(self.config_file, "r") as configfile:
                test_list = configfile.read().splitlines()
        except IOError:
            print ("Error: 'planned-tests.conf' not found!")
            print ("Aborting test session.")
            sys.exit(1)
        return test_list

    def default_port(self):
        """Get the default serial port on different platforms"""
        if platform.system() == 'Windows':
            return self.DEFAULT_PORT_WINDOWS

        return self.DEFAULT_PORT_UNIX
