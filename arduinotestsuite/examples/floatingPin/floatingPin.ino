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
}

void loop()
{
  suite.run();
}
