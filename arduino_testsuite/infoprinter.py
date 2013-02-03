""" Print information messages

This is currently used to keep the info messages out of the other code
This can later be changed to become a logging interface.

"""

from __future__ import print_function, division  # We require Python 2.6+


def double_line():
    """Print a double line"""
    print ("=============================================================")


def single_line():
    """Print a single line"""
    print ("-------------------------------------------------------------")


def top():
    """Print the top of the cli message"""
    print ("")
    double_line()
    print ("Planned tests:")


def programflow():
    """Print the program flow"""
    print ("")
    print ("Program flow: ")
    print (" 1. Compile TestSuite sketch")
    print (" 2. Upload sketch using Arscons")
    print (" 3. Check unit test output")


def planned_tests(test_list):
    """Print an overview of all the test that are planned"""
    top()
    for index, item in enumerate(test_list):
        print (" ", end="")
        print (index + 1, end="")
        print (". ", end="")
        print (item)
    programflow()


def setup_info(index, current_test):
    """Print text at start of a test."""
    print ("")
    double_line()
    print ("Starting test ", end="")
    print (index + 1, end=": ")
    print (current_test)
    single_line()
    print ("Compiling & uploading sketch to Arduino...")


def summary(failedtest_list, passedtest_list):
    """Print the summary of all the tests."""
    print ("")
    double_line()
    print ("Summary: ")
    single_line()
    print ("Failed tests:")
    for index, item in enumerate(failedtest_list):
        print (" " + str(index + 1) + "." + item)
    print ("")
    print ("Passed tests:")
    for index, item in enumerate(passedtest_list):
        print (" " + str(index + 1) + "." + item)
    double_line()
    print ("")


def upload_status(state):
    """Print info about the outcome of the upload to the Arduino board."""
    if (state == 0):
        print ("Upload succesfull")
        #print(".", end="")
    else:
        print ("Upload Failed")
