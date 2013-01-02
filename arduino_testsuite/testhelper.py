#!/usr/bin/env python
#
# Arduino TestSuite to automate unit tests on the Arduino platform
# Copyright (C) 2012  Jeroen Doggen <jeroendoggen@gmail.com>
# More info in "main.py"
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

from __future__ import print_function, division  # We require Python 2.6+

import time
import os
import subprocess
import datetime
import signal


class TestHelper:
    def timeout_command(self, command, timeout):
        #"""call shell-command and either return its output or kill it
        #if it doesn't normally exit within timeout seconds and return None"""

        cmd = command.split(" ")
        start = datetime.datetime.now()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)

        while process.poll() is None:
            now = datetime.datetime.now()
            time.sleep(1)
            if (now - start).seconds > timeout:
                print ("Process timeout")
                os.kill(process.pid, signal.SIGKILL)
                os.waitpid(-1, os.WNOHANG)
                return None
        return process.poll()

    def exitValue(self, failureCount):
        if (failureCount == 0):
            return 0
        else:
            return 42
