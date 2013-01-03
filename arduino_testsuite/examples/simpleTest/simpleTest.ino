#include <ArduinoUnit.h>

TestSuite suite ("Simple Tests");

void setup()
{
  Serial.begin(9600);
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
