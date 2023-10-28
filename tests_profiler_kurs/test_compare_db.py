from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time

#Тест сравнение сравнение двух таблиц
def test_compare_db(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("bt_tools.png")
    distance = -10
    mouse_controller = Mouse()
    current_position = mouse_controller.getPos()
    new_position = current_position.offset(0, distance)
    mouse_controller.move(new_position)
    result2 = lackey.exists("bt_tools_info.png")
    lackey.click("bt_comp_db.png")
    result3 = lackey.exists("icon_comp_db.png")
    lackey.click("bt_source_db.png")
    lackey.click("bt_phone_test.png")
    lackey.click("icon_tables_db.png")
    lackey.click("bt_compare.png")
    #result4 = lackey.exists("icon_info_message.png")
    time.sleep(2)
    lackey.type(lackey.Key.ENTER)
    result5 = lackey.exists("info_output.png")
    lackey.click("tap_view.png")
    lackey.click("tap_SQL.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    result6 = lackey.exists("info_profiler_compare_db.png")
    time.sleep(3)
    lackey.rightClick("icon_comp_db.png")
    lackey.click("bt_tab_close_all.png")
    time.sleep(3)
    assert result1 != None
    assert result2 != None
    assert result3 != None
    #assert result4 != None
    assert result5 != None
    assert result6 != None