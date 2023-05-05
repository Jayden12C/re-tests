import lackey
from re_tests_plugin import *
import pyautogui


def test_1(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("select cast(:test as integer) from rdb$database")
    lackey.click("icon_execute_query.png")
    result1 = lackey.exists("ms_input_parameters.png")
    lackey.type("123456")
    result2 = lackey.exists("ms_input_parameters_with_int.png")
    lackey.click("bt_cancel.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    assert result1 != None
    assert result2 != None