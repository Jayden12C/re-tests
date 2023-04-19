import lackey
from re_tests_plugin import *
import pyautogui


def test_1(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("select * from employee;{ENTER}select * from employee;")
    lackey.type("a", lackey.Key.CTRL)
    pyautogui.hotkey('ctrl', '/')
    time.sleep(2)
    lackey.type("z", lackey.Key.CTRL)
    result1 = lackey.find("tab_query_editor_with_comment.png")
    lackey.type("z", lackey.Key.CTRL)
    result2 = lackey.find("tab_query_editor_with_text.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    assert result1 != None
    assert result2 != None