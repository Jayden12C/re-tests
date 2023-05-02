import lackey
from re_tests_plugin import *

def test_check_show_password(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_users.png")
    lackey.click("tree_create_menu.png")
    lackey.click("text_input_password.png")
    lackey.type("123")
    result1 = lackey.exists("text_input_password_invisible.png")
    lackey.click("chb_show_pass.png")
    result2 = lackey.exists("text_input_password_visible.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_yes.png")
    assert result1 != None
    assert result2 != None

def test_check_paste_from_clipboard(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_users.png")
    lackey.click("tree_create_menu.png")
    lackey.App.setClipboard("123")
    lackey.click("chb_show_pass.png")
    lackey.click("text_input_password.png")
    print(lackey.App.getClipboard)
    lackey.type("v", lackey.Key.CTRL)
    result = lackey.exists("text_input_password_visible.png")
    lackey.click("bt_cancel.png")
    assert result != None