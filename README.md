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

Installation:
-------------
 * Downloads source and run ``python setup.py install``
 * Python Package available in the Python Package Index at: http://pypi.python.org/pypi/ArduinoTestSuite/ (``pip install ArduinoTestSuite``)
 * Currently only tested on Linux (subprocess handling only works on Linux)

Usage:
------
 * Start the program with: ``python -m ArduinoTestSuite`` (or ``python main.py``)
 * Select the tests you want to run by editing: ``planned-tests.conf``
 * Other configuration options: ``python -m ArduinoTestSuite --help``

References
----------
 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons

Typical Output:
---------------
In this examples, two Arduino libraries are tested, one passes, one fails.

````
=============================================================
Planned tests:
-------------------------------------------------------------
 1. DistanceSensor/examples/GP2Y0A21YK/TestSuite/
 2. My_Module/examples/TestSuite/

Program flow:
 1. Compile TestSuite sketch
 2. Upload sketch using Arscons
 3. Check unit test output

=============================================================
Starting test: DistanceSensor/examples/GP2Y0A21YK/TestSuite/
-------------------------------------------------------------
Compiling & uploading sketch to Arduino...
Upload succesfull
Running test suite...
Tests run: 3 Successful: 3 Failed: 0

=============================================================
Starting test: My_Module/examples/TestSuite/
-------------------------------------------------------------
Compiling & uploading sketch to Arduino...
Upload succesfull
Running test suite...
Assertion failed in 'temperatureRange' on line 68
Tests run: 3 Successful: 2 Failed: 1

=============================================================
Summary: 
Failed tests:
 1. My_Module/examples/TestSuite/

Passed tests:
 1. DistanceSensor/examples/GP2Y0A21YK/TestSuite/
=============================================================
````
