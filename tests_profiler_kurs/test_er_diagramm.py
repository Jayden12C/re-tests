from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time
import os


def move_mouse(distance):
    mouse_controller = Mouse()
    current_position = mouse_controller.getPos()
    new_position = current_position.offset(distance, 0)
    mouse_controller.move(new_position)


def move_mouse_to_target(target_image):
    lackey.SettingsMaster.MinSimilarity = 0.7
    move_location = lackey.find(target_image).getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)

#Тест построение er диаграммы
def test_er_diagramm(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("bt_view_extended.png")
    lackey.click("icon_bt_database.png")
    time.sleep(1)
    result2 = lackey.exists("icon_database_open.png")
    move_mouse_to_target("str_menu_generate_erd.png")
    lackey.click("map_er.png")
    time.sleep(1)
    result3 = lackey.exists("info_new_connections.png")
    lackey.click("table_name_EMPLOYEE.png")
    lackey.click("bt_triangle_right.png")
    lackey.click("department.png")
    lackey.click("bt_triangle_right.png")
    lackey.click("bt_generate.png")
    lackey.rightClick()
    distance = -20
    move_mouse(distance)
    time.sleep(1)
    result4 = lackey.exists("bt_right_info.png")
    move_mouse_to_target("bt_view.png")
    time.sleep(1)
    distance2 = 80
    move_mouse(distance2)
    lackey.click("bt_format_125.png")
    time.sleep(2)
    result5 = lackey.exists("er_diagram.png")
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)
    lackey.rightClick("tab_erd_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None
