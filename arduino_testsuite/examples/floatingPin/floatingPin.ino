#include <ArduinoUnit.h>
#include <TestHelper.h>

TestSuite suite;
TestHelper helper;

test(floatingInputPin)
{
  assertTrue(!(helper.floatingInputPin(A0)));     // true means: no floating input pins -> test passed
}

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  suite.run();
}
