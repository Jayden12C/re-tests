import lackey
from re_tests_plugin import *
import time
import os
import platform

#Тест экспорт результата в файл с инструментом профайлер
def test_export_result(open_connection):
    #Перед началом теста укажите в тесте и Red Expert где будет папка test.txt
    current_os = platform.system()
    if current_os == "Windows":
        file_path = 'D:\\study\\Leto\\re-tests\\files\\test.txt'
        file = open(file_path, 'w')
        file.close()
    elif current_os == "Linux":
        file_path = "/var/lib/test.txt"
        file = open(file_path, 'w')
        file.close()
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("icon_bt_database.png")
    lackey.click("bt_export_result.png")
    result2 = lackey.exists("icon_tab_export.png")
    lackey.click("bt_browse.png")
    lackey.doubleClick("txt_files.png")
    lackey.type(lackey.Key.ENTER)
    time.sleep(2)
    lackey.click("tab_query_editor_text.png")
    sql_request = """SELECT E.FIRST_NAME, E.LAST_NAME, E.Salary, E.JOB_COUNTRY, D.DEPARTMENT FROM Employee E INNER JOIN DEPARTMENT D ON E.DEPT_NO = D.DEPT_NO WHERE E.JOB_COUNTRY = 'USA' ORDER BY E.Salary DESC;"""
    lackey.type(sql_request)
    lackey.click("bt_execute_icon.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
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
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    os.remove(file_path)
    assert result1 != None
    assert result2 != None