Arduino TestSuite: Automated Arduino Unit Tests
===============================================
This Python scripts allows automated running of several Arduino unit tests.
The testing process is started on the PC but the tests run on the actual Arduino hardware.
One set of unit tests is typically used to test one Arduino library.

The following steps are performed for each set of unit tests:
 1. The script compiles and uploads an Arduino sketch that contains the unit testing.
 2. The unit tests are run on the Arduino board.
 3. The results of the test are printed over the serial port and analyzed by the Python script.
 4. The script starts the next test, repeating steps 1,2 and 3 for all test that are requested in the configuration file.
    The script prints a summary showing an overview of all the failed/passed tests in the complete testsuite.

Installation:
-------------
 * Download the source and run ``python setup.py install``
 * Python Package available in the Python Package Index at: http://pypi.python.org/pypi/arduino_testsuite
 * Install using pip: ``pip install ArduinoTestSuite``

Usage:
------
 * Start the program with: ``python -m arduino_testsuite`` (or ``python main.py``)
 * Select the tests you want to run by editing: ``planned-tests.conf``
 * Getting help: ``python -m arduino_testsuite --help``
 * Post issues to GitHub <http://github.com/jeroendoggen/Arduino-TestSuite/issues>.

Requirements:
-------------
 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons
 * Python 2.6+ packages: pyserial

Limitations:
------------
 * Currently only tested on Linux

  * Default paths are configured for Linux
  * Subprocess handling only works on Linux

 * The program was created with other OS users in mind, so it will eventually get full cross-platform support. Help from Windows-developers is much appreciated.

License:
--------
If not stated otherwise ArduinoTestSuite is distributed in terms of the GPLv2 software license.
See COPYING in the distribution for details.

Bug reports:
------------
 * Jeroen Doggen <jeroendoggen@gmail.com>

Changelog:
----------
0.2.2: Error handling:
 * Compile & upload errors
 * Timing: timeout for uploading & running of the tests
 * Missing files: wrong test folder, no config file
 * Hardware: Disconnect Arduino during test

0.2.1: Settings & configuration
 * Passing cli arguments & cli help messages
 * Settings separated from other code
 * Start tests from config file

0.2: First working OOP version
 * Subprocess for arscons
 * Classes: Test, TestSuite, InfoPrinter
 * Divided the code in several modules

0.1: Initial release:
 * Call scons
 * Run unit test
 * Print summary
