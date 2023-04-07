import lackey
from re_tests_plugin import *

def test_1(open_connection):
    lackey.click("files/images/tree_plus.png")
    all_plus = lackey.findAll("files/images/tree_plus.png")
    lackey.click(list(all_plus)[2])
    lackey.doubleClick("files/images/tree_table_name_EMPLOYEE.png")
    lackey.click("files/images/tab_triggers.png")
    lackey.doubleClick("files/images/trigger_name.png")
    time.sleep(2)
    lackey.type("{ESC}")
    result = lackey.find("files/images/trigger_name.png")
    lackey.rightClick("files/images/tab_table_EMPLOYEE_blue.png")
    lackey.click("files/images/bt_tab_close_all.png")
    assert result != None, "List of triggers is empty"