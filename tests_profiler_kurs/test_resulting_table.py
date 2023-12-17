from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time
from lackey.InputEmulation import Mouse


def test_resulting_table(open_connection):
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
    lackey.type("100")
    lackey.click("bt_OK.png")
    time.sleep(3)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("info_profiler_execute.png")
    lackey.type(lackey.Key.ADD)
    lackey.type(lackey.Key.DOWN)
    lackey.type(lackey.Key.ADD)
    lackey.type(lackey.Key.DOWN)
    lackey.type(lackey.Key.ADD)
    time.sleep(3)
    lackey.click("icon_columns_process_name.png")
    time.sleep(3)
    lackey.click()
    time.sleep(3)
    lackey.click("icon_columns_total_time.png")
    time.sleep(3)
    lackey.click()
    time.sleep(3)
    lackey.click("icon_columns_average_time.png")
    time.sleep(3)
    lackey.click()
    time.sleep(3)
    lackey.click("icon_columns_calls_count.png")
    time.sleep(3)
    lackey.click()
    time.sleep(3)
    lackey.click("bt_discard.png")
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None