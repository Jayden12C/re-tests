
import lackey
from re_tests_plugin import *
import time
from lackey.InputEmulation import Mouse

def move_mouse(distance):
    mouse_controller = Mouse()
    current_position = mouse_controller.getPos()
    new_position = current_position.offset(distance, 0)
    mouse_controller.move(new_position)


def test_pop_up_window_profiler(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    result2 = lackey.exists("tab_query_editor_text.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("""SELECT
    Dept_NO,
    COUNT(EMP_NO) AS TotalEmployees,
    AVG(Salary) AS AverageSalary FROM Employee GROUP BY Dept_NO;""")
    lackey.click("bt_format_sql.png")
    lackey.click("icon_execute_query.png")
    time.sleep(3)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(4)
    lackey.click("icon_session.png")
    lackey.type(lackey.Key.DOWN)
    lackey.rightClick("sql_scripts_profiler.png")
    distance = -30
    move_mouse(distance)
    result3 = lackey.exists("icon_pop_up_window.png")
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