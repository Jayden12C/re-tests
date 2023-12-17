import time
import lackey
from re_tests_plugin import *

#Тестирование кнопки выполнение sql запросов в профайлере
def test_sql_request1(open_connection):
    lackey.click("tab_query_editor.png")
    sql_requst = "SELECT * FROM employee WHERE DEPT_NO = 621 or DEPT_NO = 623;"
    time.sleep(1)
    lackey.click("tab_query_editor_text.png")
    lackey.type(sql_requst)
    lackey.click("bt_execute_profiler.png")
    time.sleep(3)
    result2 = lackey.exists("icon_session.png")
    lackey.click("tab_info_request1_profiler.png")
    lackey.rightClick("tab_info_request1_profiler.png")
    lackey.click("bt_info.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.click("bt_discard.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    lackey.rightClick("icon_tab_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result2 != None

def test_sql_request2(open_connection):
    lackey.click("tab_query_editor.png")
    sql_requst = """SELECT e.FIRST_NAME || ' ' || e.LAST_NAME AS Employee_Name,d.DEPT_NO AS Department,SUM(e.SALARY) AS Salary FROM employee e JOIN department d ON e.DEPT_NO = d.DEPT_NO GROUP BY e.FIRST_NAME,e.LAST_NAME, d.DEPT_NO ORDER BY Salary DESC; """
    lackey.click("tab_query_editor_text.png")
    lackey.type(sql_requst)
    lackey.click("bt_format_sql.png")
    lackey.click("bt_execute_profiler.png")
    time.sleep(4)
    result2 = lackey.exists("icon_session.png")
    lackey.click("tab_info_request2_profiler.png")
    lackey.rightClick("tab_info_request2_profiler.png")
    lackey.click("bt_info.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.click("bt_discard.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    lackey.rightClick("icon_tab_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result2 != None

def test_command_history(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    result2 = lackey.exists("tab_query_editor_text.png")
    lackey.click("icon_show_history.png")
    result3 = lackey.exists("comand_history.png")
    requst = "DEPT_NO = 621 or DEPT_NO = 623"
    lackey.type(requst)
    lackey.click("bt_search.png")
    lackey.type(lackey.Key.ENTER)
    lackey.click("bt_select.png")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("tab_info_request1_profiler.png")
    lackey.rightClick("tab_info_request1_profiler.png")
    lackey.click("bt_info.png")
    time.sleep(3)
    lackey.type(lackey.Key.ESC)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
