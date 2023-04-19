import lackey
from re_tests_plugin import *

def test_check_PID():
    assert  lackey.App("Red Expert").getPID() != -1, "RedExpert not running"