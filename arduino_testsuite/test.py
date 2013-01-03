

import unittest
import random

from arduino_testsuite.testhelper import TestHelper

helper = TestHelper()


class testArduino(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_runArduinoTests(self):
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
