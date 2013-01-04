#include <ArduinoUnit.h>

TestSuite suite ("Slow test (with a 10s delay)");

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
  delay(10000);
  // Run test suite, printing results to the serial port
  suite.run();
}
