#include <ArduinoUnit.h>

TestSuite suite ("Slow test (with a 10s delay)");

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
  delay(10000);
  // Run test suite, printing results to the serial port
  suite.run();
}