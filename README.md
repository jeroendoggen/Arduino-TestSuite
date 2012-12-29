Arduino TestSuite
=================

Python Script to automate Arduino Unit Tests
--------------------------------------------
This Python scripts allows automated running of several Arduino unit tests.
The testing process is started on the PC but the tests run on the actual Arduino hardware.
One set of unit tests is typically used to test one Arduino library.

The following steps are performed for each set of unit tests:
 1. The scipts compiles and uploads a sketch that contains the unit testing code to the Arduino board.
 2. The unit test are run on the Arduino board.
 3. The results of the test are printed over the serial port and analyzed by this Python scripts
 4. The script start the next test. Steps 1,2 and 3 are repeated for all the libraries that you are using in the project.
  The script prints a summary showing an overview of the failed/passed test in the complete testsuite.

Installation:
-------------
 * Downloads source and run "python setup.py install"
 * Python Package available in the Python Package Index at: http://pypi.python.org/pypi/ArduinoTestSuite/ ("pip install ArduinoTestSuite")
 * Currently only tested on Linux (serial port is hardcoded, subprocess handling only works on Linux)

Usage:
------
 * Start the program with: "python -m ArduinoTestSuite" (or python main.py)
 * Selecting the tests you want to run, configuring Arduino path and configuring the serial port is currently done by editing "main.py" and "testSuite.py"

References
----------
 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons

Typical Output:
---------------
Two Arduino libraries are tested, one passes, one fails.

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
