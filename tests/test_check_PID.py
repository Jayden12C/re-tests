import lackey
from re_tests_plugin import *

def test_check_PID(open_connection):
    assert  lackey.App("Red Expert").getPID() != -1, "RedExpert not running"