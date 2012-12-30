#include <ArduinoUnit.h>
#include <TestHelper.h>

TestSuite suite ("In Interval");
TestHelper helper;

void setup()
{
}

test(interval)
{
  assertTrue(helper.inInterval(5,2,6));           // (data,lower,upper)
}

void loop()
{
  // Run test suite, printing results to the serial port
  suite.run();
}
