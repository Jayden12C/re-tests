import time
import lackey
from re_tests_plugin import *

def test_sql_requst1(open_connection):
    start_time = time.time()
    sql_requst = "SELECT * FROM employee WHERE DEPT_NO = 621 or DEPT_NO = 623"
    lackey.click("tab_query_editor_text.png")
    lackey.type(sql_requst)
    end_time = time.time()
    lackey.click("icon_execute_query.png")
    execution_time = end_time - start_time
    print(f"Время выполнения SQL запроса: {execution_time} секунд")
    time.sleep(5)
    result = lackey.exists("icon_table_sql_requst.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    assert result != None

def test_sql_requst2(open_connection):
    start_time = time.time()
    sql_requst = """SELECT e.FIRST_NAME || ' ' || e.LAST_NAME AS Employee_Name,d.DEPT_NO AS Department,SUM(e.SALARY) AS Salary FROM employee e JOIN department d ON e.DEPT_NO = d.DEPT_NO GROUP BY e.FIRST_NAME,e.LAST_NAME, d.DEPT_NO ORDER BY Salary DESC; """
    lackey.click("tab_query_editor_text.png")
    lackey.type(sql_requst)
    lackey.click("bt_format_sql.png")
    end_time = time.time()
    lackey.click("icon_execute_query.png")
    execution_time = end_time - start_time
    print(f"Время выполнения SQL запроса: {execution_time} секунд")
    time.sleep(5)
    result = lackey.exists("icon_table_sql_requst2.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    assert result != None

def test_command_history(open_connection):
    result1 = lackey.exists("tab_query_editor_text.png")
    lackey.click("icon_show_history.png")
    result2 = lackey.exists("comand_history.png")
    requst = "DEPT_NO = 621 or DEPT_NO = 623"
    lackey.type(requst)
    lackey.click("bt_search.png")
    lackey.type(lackey.Key.ENTER)
    lackey.click("bt_select.png")
    time.sleep(5)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("s", lackey.Key.CTRL)
    assert result1 != None
    assert result2 != None