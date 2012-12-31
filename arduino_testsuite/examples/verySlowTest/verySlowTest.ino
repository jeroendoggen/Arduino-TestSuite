#include <ArduinoUnit.h>

TestSuite suite ("Very slow test (with a 20s delay)");

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
  delay(20000);
  // Run test suite, printing results to the serial port
  suite.run();
}