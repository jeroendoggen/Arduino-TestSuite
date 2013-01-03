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
