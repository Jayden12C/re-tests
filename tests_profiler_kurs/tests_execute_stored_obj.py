from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time

#Тестирование выполнить сохраненный объект
def test_execute_stored_obj1(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("bt_execute.png")
    result2 = lackey.exists("icon_execute_st.png")
    lackey.click("bt_obj_name.png")
    lackey.click("bt_budgept.png")
    lackey.click("bt_execute_icon.png")
    lackey.type("000")
    lackey.click("bt_OK.png")
    time.sleep(3)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("info_profiler_execute.png")
    lackey.click("tree_blue.png")
    lackey.click("bt_exe_budgept.png")
    lackey.rightClick()
    lackey.click("bt_show.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None

def test_execute_stored_obj2(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("bt_execute.png")
    result2 = lackey.exists("icon_execute_st.png")
    lackey.click("bt_obj_name.png")
    lackey.click("bt_get_EMP.png")
    lackey.click("bt_execute_icon.png")
    lackey.type("113")
    lackey.click("bt_OK.png")
    time.sleep(3)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("bt_exe_EMP.png")
    lackey.click("tree_blue.png")
    lackey.click("icon_EMP_proj.png")
    lackey.rightClick()
    lackey.click("bt_show.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None

