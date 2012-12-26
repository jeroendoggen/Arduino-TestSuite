Arduino TestSuite
-----------------

### Python Script to automate Arduino Unit Tests

 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons

### Program Flow: 
These steps are performed for each set of unit tests (typically to test one Arduino library)
   1. Compile a sketch that runs several unit tests
   2. Upload and run the sketch using Arscons
   3. Check unit test output

Steps 1,2 and 3 are repeated for all the libraries that you are using in the project.

The script prints a summary showing an overview of the failed/passed test in the complete testsuite.

### Typical Output:
````
================================================================================
Planned tests:
 1. DistanceSensor/examples/GP2Y0A21YK/TestSuite/
 2. My_Module/examples/TestSuite/

Program flow: 
 1. Compile TestSuite sketch
 2. Upload sketch using Arscons
 3. Check unit test output

================================================================================
Starting test: DistanceSensor/examples/GP2Y0A21YK/TestSuite/
--------------------------------------------------------------------------------
Running test suite...
Tests run: 3 Successful: 3 Failed: 0

================================================================================
Starting test: My_Module/examples/TestSuite/
--------------------------------------------------------------------------------
Running test suite...
Assertion failed in 'temperatureRange' on line 68
Tests run: 3 Successful: 2 Failed: 1

================================================================================
Summary: 
Failed tests:
 1. My_Module/examples/TestSuite/

Passed tests:
 1. DistanceSensor/examples/GP2Y0A21YK/TestSuite/
================================================================================
````
