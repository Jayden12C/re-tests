import lackey

def test_check_PID():
    assert  lackey.App("Red Expert").getPID() != -1, "RedExpert not running"