""" Arduino TestSuite to automate unit tests on the Arduino platform

This file is needed to import the module properly
Copyright (C) 2012  Jeroen Doggen <jeroendoggen@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA  02110-1301, USA.

"""

import sys

from arduino_testsuite.testsuite import TestSuite


def run():
    """Run the main program"""
    suite = TestSuite()
    timeout = 10
    suite.printPlannedTests()
    suite.runTests(timeout)
    suite.printSummary()
    return(suite.exitValue())


if __name__ == "__main__":
    sys.exit(run())
