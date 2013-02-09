""" arduino_testsuite: core code

This is currently used to keep the info messages out of the other code
This can later be changed to become a logging interface.

"""
from __future__ import print_function, division  # We require Python 2.6+

import os
import time
import datetime
import platform

import infoprinter
import testhelper
from arduino_testsuite.settings import Settings


class TestSuite:
    """TestSuite class: does the core of the work"""
    not_finished = True    # boolean value
    found_test_path = False
    upload_status = False
    failed_test_list = []
    passed_test_list = []
    failure_count = 0
    line = []
    test_list = []
    config = Settings()
    scriptpath = os.getcwd()

    def __init__(self):
        """Initialize the suite: cli, config file."""
        self.config.get_cli_arguments()
        self.test_list = self.config.read_testlist_file()

    def print_planned_tests(self):
        """Print an overview of all the test that are planned"""
        infoprinter.planned_tests(self.test_list)
        infoprinter.programflow()

    def run_tests(self, timeout):
        """Run all the tests"""
        for index, current_test in enumerate(self.test_list):
            self.goto_testpath(index, current_test)
            if (self.found_test_path):
                self.found_test_path = False
                print("Starting upload...")
                self.upload_sketch(timeout)
                if (self.upload_status == 0):
                    print("Start tests...")
                    self.analyze_output(timeout, current_test)
                else:
                    self.failed_test_list.append(current_test)

    def goto_testpath(self, index, current_test):
        """Go to the folder of the current test"""
        infoprinter.setup_info(index, current_test)
        try:
            os.chdir(self.scriptpath)
        except OSError:
            print("Error: unable to open the script folder")
            print("This should never happen...")
        try:
            os.chdir(current_test)
            self.found_test_path = True
        except OSError:
            print("Error: unable to open test folder")
            print("Check your config file")
            self.found_test_path = False
            self.failed_test_list.append(current_test)

    def upload_sketch(self, timeout):
        """Upload the sketch to the Arduino board"""
        scons_command = "scons"
        if platform.system() == 'Windows':
            scons_command += ".bat"
        sconstruct_dir_argument = "--directory=" + os.getcwd()
        port_argument = "ARDUINO_PORT=" + self.config.serial_port
        board_argument = "ARDUINO_BOARD=" + self.config.board
        self.upload_status = testhelper.timed_cmd(
          scons_command + " " +
          sconstruct_dir_argument + " " +
          port_argument + " " +
          board_argument + " " +
          "upload", timeout)
        infoprinter.upload_status(self.upload_status)

    def analyze_output(self, timeout, current_test):
        """Analyze the test output that is received over the serial port"""
        self.ser = self.config.init_serial_port()

        start = datetime.datetime.now()
        while self.not_finished:
            self.read_line(current_test)
            time.sleep(0.1)
            now = datetime.datetime.now()
            if (now - start).seconds > timeout:
                print ("Test timeout after ", end="")
                print (timeout, end="")
                print (" seconds")
                self.not_finished = False
        self.not_finished = True   # to allow the next test to start
        if (self.line[11] == self.line[25]):
            if current_test not in self.failed_test_list:
                self.passed_test_list.append(current_test)
        else:
            self.failed_test_list.append(current_test)
            self.failure_count = self.failure_count + 1

        self.ser.close()

    def read_line(self, current_test):
        """Read one line of text over the serial port"""
        try:
            self.line = self.ser.readline().decode('utf-8')[:-1]
            print (self.line)
        except IOError:
            print ("unexpectedly lost serial connection")
            self.failed_test_list.append(current_test)
        if(self.line.find("Tests run:") == 0):
            self.not_finished = False

    def print_summary(self):
        """Print the summary of all the tests."""
        infoprinter.summary(self.failed_test_list, self.passed_test_list)

    def exit_value(self):
        """Generate the exit value for the application."""
        if (self.failure_count == 0):
            return 0
        else:
            return 42
