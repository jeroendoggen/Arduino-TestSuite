Arduino-TestSuite
-----------------

### Arduino TestSuite to automate Arduino unit tests

 * The unit tests are written using the Arduinounit library: http://code.google.com/p/arduinounit
 * The tests my unit test helper class: http://code.google.com/p/arduino-unit-test-helper-library
 * The code is uploaded to the Arduino board using Arscons: http://code.google.com/p/arscons/

### Program flow: 
 * Start test 1
   1. Compile a sketch that runs several unit tests
   2. Upload and run the sketch using Arscons
   3. Check unit test output
 * Start test 2
   * Repeat steps 1, 2, 3
 * Print summary
