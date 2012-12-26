Arduino-TestSuite
-----------------

### Arduino TestSuite to automate Arduino unit tests

 * The unit tests are written with the "Arduino Unit Testing Library": http://code.google.com/p/arduinounit
 * The tests also use "Arduino Unit Testing Helper Library": http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board with "Arscons: scons script for Arduino": http://github.com/suapapa/arscons

### Program flow: 
These steps are performed for each set of unit tests (typically to test one Arduino library)
   1. Compile a sketch that runs several unit tests
   2. Upload and run the sketch using Arscons
   3. Check unit test output

Steps 1,2 and 3 are repeated for all the libraries that you are using in the project.

The script prints a summary showing an overview of the failed/passed test in the complete testsuite.
