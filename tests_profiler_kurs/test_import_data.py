import time
from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *


def move_mouse(distance):
    mouse_controller = Mouse()
    current_position = mouse_controller.getPos()
    new_position = current_position.offset(0, distance)
    mouse_controller.move(new_position)

def test_import_data():
    if lackey.exists("icon_phone_test.png"):
        lackey.click("icon_phone_test.png")
        lackey.click("icon_disconnected.png")
    elif lackey.exists("icon_phone_test_clicked.png"):
        lackey.click("icon_disconnected.png")
    else:
        pass
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    result2 = lackey.exists("tab_query_editor_text.png")
    create_table_sql1 = """CREATE TABLE Titanic (
    NAME VARCHAR(1024),
    SEX CHAR(6),
    TICKET VARCHAR(255)
);"""
    lackey.type(create_table_sql1)
    lackey.click("bt_format_sql.png")
    lackey.click("icon_execute_query.png")
    lackey.click("icon_bt_database.png")
    lackey.click("bt_import_data.png")
    result3 = lackey.exists("icon_import.png")
    lackey.click("icon_select_delimitr.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(",")
    lackey.click("bt_browse.png")
    lackey.doubleClick("titanic_csv.png")
    lackey.click("bt_read_file.png")
    lackey.click("bt_source.png")
    lackey.click("icon_select_table.png")
    move_mouse(15)
    time.sleep(2)
    mouse = Mouse()
    direction = Mouse.WHEEL_DOWN
    steps = 1
    mouse.wheel(direction, steps)
    lackey.click("bt_TITANIC.png")
    lackey.click("icon_file_mapping.png")
    lackey.click("NAME.png")
    lackey.click("source_column.png")
    lackey.click("icon_name.png")
    time.sleep(1)
    lackey.type(lackey.Key.DOWN)
    lackey.click("source_column.png")
    lackey.click("icon_sex.png")
    time.sleep(1)
    lackey.type(lackey.Key.DOWN)
    lackey.click("source_column.png")
    move_mouse(15)
    mouse.wheel(direction, steps)
    lackey.click("icon_ticket.png")
    lackey.click("bt_import.png")
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)
    lackey.click("bt_resume.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("SELECT * FROM TITANIC;")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("DROP TABLE TITANIC;")
    lackey.click("icon_execute_query.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    lackey.click("icon_connected.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
