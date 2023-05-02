import lackey
from re_tests_plugin import *

def test_window_authorized_site():
    lackey.click("bt_site_not_authorized.png")
    lackey.click("text_input_user.png")
    lackey.type("nikita.kashin")
    lackey.type("{TAB}")
    lackey.type("123")
    lackey.type("{TAB}")
    lackey.type("{ENTER}")
    lackey.SettingsMaster.MinSimilarity = 0.7
    result = lackey.exists("text_input_password_visible.png")
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.click("bt_cancel.png")
    assert result != None