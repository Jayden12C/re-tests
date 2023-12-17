import lackey
from re_tests_plugin import *
import time
#Тестирование Менеджер пользователей с инструментом профайлере
def test_user_manager(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("bt_user_manager.png")
    time.sleep(2)
    result2 = lackey.exists("icon_user_manager.png")
    lackey.click("bt_roles.png")
    time.sleep(2)
    lackey.click("bt_membership.png")
    time.sleep(2)
    lackey.click("bt_role.png")
    lackey.click("icon_tab_profiler.png")
    time.sleep(2)
    result3 = lackey.exists("bt_icons_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(4)
    lackey.click("icon_session.png")
    lackey.type(lackey.Key.DOWN)
    lackey.rightClick("sql_scripts_profiler.png")
    lackey.click("bt_show.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.rightClick("sql_scripts_profiler.png")
    lackey.click("bt_info.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.click("bt_discard.png")
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None