THIS WILL GENERATE A BUILD ERROR
#include <ArduinoUnit.h>

TestSuite suite ("Simple Tests");

void setup()
{
}

test(Passing)
{
  assertTrue("True");
}

test(Failing)
{
  assertTrue("False");
}

void loop()
{
  // Run test suite, printing results to the serial port
  suite.run();
}