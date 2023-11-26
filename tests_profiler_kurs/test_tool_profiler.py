import time
import lackey
from re_tests_plugin import *


def test_open_profiler_no_connections():
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result = lackey.exists("icon_error_message.png")
    time.sleep(2)
    lackey.type(lackey.Key.ENTER)
    assert result != None


def test_button_click_profiler(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("bt_pause.png")
    result2 = lackey.exists("icon_error_message2.png")
    time.sleep(2)
    lackey.type(lackey.Key.ENTER)
    lackey.click("bt_resume.png")
    lackey.click("bt_stop.png")
    result3 = lackey.exists("icon_error_message2.png")
    time.sleep(2)
    lackey.type(lackey.Key.ENTER)
    lackey.click("bt_start.png")
    lackey.click("bt_execute.png")
    result4 = lackey.exists("icon_execute_st.png")
    lackey.click("bt_obj_name.png")
    lackey.click("org_chart.png")
    lackey.click("bt_execute_icon.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("icon_org_procedura.png")
    lackey.type(lackey.Key.ADD)
    lackey.type(lackey.Key.DOWN)
    time.sleep(2)
    lackey.click("bt_default_view.png")
    lackey.click("icon_org_procedura.png")
    lackey.type(lackey.Key.ADD)
    lackey.type(lackey.Key.DOWN)
    time.sleep(2)
    lackey.click("bt_view_extended.png")
    lackey.click("icon_org_procedura.png")
    lackey.type(lackey.Key.ADD)
    lackey.type(lackey.Key.DOWN)
    lackey.type(lackey.Key.ADD)
    time.sleep(3)
    lackey.click("bt_discard.png")
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None