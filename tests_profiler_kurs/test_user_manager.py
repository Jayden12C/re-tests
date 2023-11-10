from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time

def test_user_manager(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("bt_user_manager.png")
    time.sleep(2)
    result3 = lackey.exists("icon_user_manager.png")
    lackey.click("bt_roles.png")
    time.sleep(2)
    lackey.click("bt_membership.png")
    time.sleep(2)
    lackey.click("bt_role.png")
    lackey.click("icon_tab_profiler.png")
    result4 = lackey.exists("bt_icons_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(4)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result3 != None
    assert result4 != None