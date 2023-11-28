import lackey
from re_tests_plugin import *
import time

#Тестирование оптимизированного запроса
def test_optimaze_sql(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    sql_requst = """SELECT e.first_name, e.last_name, e.salary FROM employee e WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.job_code = e.job_code
    AND e2.job_grade = e.job_grade
    AND e2.job_country = e.job_country
    AND e2.dept_no = e.dept_no
);"""
    lackey.type(sql_requst)
    lackey.click("bt_format_sql.png")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)

    lackey.click("bt_resume.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    sql_requst1 = """SELECT first_name, last_name, salary FROM (
    SELECT e.first_name, e.last_name, e.salary,
           AVG(e.salary) OVER (PARTITION BY e.job_code, e.job_grade, e.job_country, e.dept_no) AS avg_salary FROM employee e
) AS subquery WHERE salary > avg_salary;"""
    lackey.type(sql_requst1)
    lackey.click("bt_format_sql.png")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(5)
    lackey.click("bt_discard.png")
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None