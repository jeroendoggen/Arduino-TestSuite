Arduino TestSuite: Python Script to automate Arduino Unit Tests
===============================================================

This Python scripts allows automated running of several Arduino unit tests.
The testing process is started on the PC but the tests run on the actual Arduino hardware.
One set of unit tests is typically used to test one Arduino library.

The following steps are performed for each set of unit tests:
 1. The script compiles and uploads an Arduino sketch that contains the unit testing.
 2. The unit tests are run on the Arduino board.
 3. The results of the test are printed over the serial port and analyzed by the Python script.
 4. The script starts the next test, repeating steps 1,2 and 3 for all test that are requested in the configuration file.
  The script prints a summary showing an overview of all the failed/passed tests in the complete testsuite.

Usage:
------
 * Start the program with: "python -m ArduinoTestSuite" (or python main.py)
 * Select the tests you want to run by editing: "planned-tests.conf"
 * Other configuration options: "python -m ArduinoTestSuite --help"

References
----------
 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons

Known issues:
-------------
 * Does not work with Python3 (because of Scons)

Bug reports:
------------
 * Jeroen Doggen <jeroendoggen@gmail.com>
