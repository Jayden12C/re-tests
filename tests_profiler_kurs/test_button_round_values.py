import lackey
from re_tests_plugin import *
import time


def test_button_round_values(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("bt_execute.png")
    result2 = lackey.exists("icon_execute_st.png")
    lackey.click("bt_obj_name.png")
    lackey.click("bt_budgept.png")
    lackey.click("bt_execute_icon.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("000")
    lackey.click("bt_OK.png")
    time.sleep(3)
    lackey.click("bt_budgept.png")
    lackey.click("bt_get_EMP.png")
    lackey.click("bt_execute_icon.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("113")
    lackey.click("bt_OK.png")
    time.sleep(3)
    lackey.click("bt_get_EMP.png")
    lackey.click("bt_mail_label.png")
    lackey.click("bt_execute_icon.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("1001")
    lackey.click("bt_OK.png")
    time.sleep(4)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)

    lackey.click("icon_round_values.png")
    time.sleep(2)
    lackey.click()
    time.sleep(2)
    lackey.click("bt_discard.png")
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
