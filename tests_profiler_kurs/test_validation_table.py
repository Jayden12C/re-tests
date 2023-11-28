import lackey
from re_tests_plugin import *
import time
#Тестирование валидации таблиц с инструментом профайлер
def test_validation(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    time.sleep(2)
    lackey.click("bt_tools.png")
    lackey.click("bt_validation.png")
    result2 = lackey.exists("icon_validation_table.png")
    time.sleep(2)
    lackey.click("table_name_EMPLOYEE.png")
    lackey.click("bt_triangle_right.png")
    lackey.click("department.png")
    lackey.click("bt_triangle_right.png")
    lackey.click("bt_start.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
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