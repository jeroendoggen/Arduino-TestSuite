""" arduino_testsuite: Test helper functions

run a command with a given timeout
return the exit value for the program

"""

from __future__ import print_function, division  # We require Python 2.6+

import time
import subprocess
import datetime
import os
import sys

def timed_cmd(command, timeout):
    """Call a cmd and kill it after 'timeout' seconds"""
    cmd = command.split(" ")
    start = datetime.datetime.now()
    workingDir = os.path.dirname(sys.executable)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE, cwd=os.path.join(workingDir, "Scripts"))

    while process.poll() is None:
        now = datetime.datetime.now()
        time.sleep(1)
        if (now - start).seconds > timeout:
            print ("Process timeout")
            process.terminate()
            return None
    return process.poll()
