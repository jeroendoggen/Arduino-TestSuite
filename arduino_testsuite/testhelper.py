""" arduino_testsuite: Test helper functions

run a command with a given timeout
return the exit value for the program

"""

from __future__ import print_function, division  # We require Python 2.6+

import time
import os
import subprocess
import datetime
import signal


def timed_cmd(command, timeout):
    """Call a cmd and kill it after 'timeout' seconds"""
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
