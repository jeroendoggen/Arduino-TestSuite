""" arduino_testsuite: Unit tests

nothing useful in here at the moment

"""

import unittest


class ArduinoTestSuite(unittest.TestCase):
    """Test the Arduino

    this part of the code could/should be called by 'nose' in the future

    """

    def setup(self):
        """Do the test setup"""
        pass

    def test_run_arduino_tests(self):
        """Run the tests on the hardware"""
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
