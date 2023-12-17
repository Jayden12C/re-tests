import lackey
from re_tests_plugin import *
import time


def data_generator():
    lackey.click("bt_tools.png")
    lackey.click("bt_generate_table.png")
    result1 = lackey.exists("icon_generator_data.png")
    time.sleep(2)
    lackey.click("icon_employeeid.png")
    lackey.click("bt_selected_delected.png")
    #lackey.click("bt_get_from_other_table.png")
    lackey.click("bt_start.png")
    lackey.type(lackey.Key.ENTER)
    assert result1 != None


#Тестирование генератор тестовых данных с инструментом профайлер
def test_data_generator():
    if lackey.exists("icon_phone_test.png"):
        lackey.click("icon_phone_test.png")
        lackey.click("icon_disconnected.png")
    elif lackey.exists("icon_phone_test_clicked.png"):
        lackey.click("icon_disconnected.png")
    else:
        pass
    time.sleep(1)
    lackey.doubleClick("tree_plus.png")
    lackey.doubleClick("icon_table.png")
    lackey.type(lackey.Key.ADD)
    if lackey.exists("tree_table_name_EMPLOYEE.png"):
        lackey.click("bt_tools.png")
        lackey.click("bt_profiler.png")
        result2 = lackey.exists("icon_info_profiler.png")
        lackey.click("bt_view_extended.png")
        lackey.click("bt_start.png")
        time.sleep(2)
        data_generator()
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
        assert result2 != None
    else:
        lackey.click("tab_query_editor.png")
        time.sleep(1)
        lackey.click("tab_query_editor_text.png")
        sql = """CREATE TABLE Employee  ( 
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary DECIMAL(10, 2)
); """
        lackey.type(sql)
        lackey.click("bt_format_sql.png")
        lackey.click("icon_execute_query.png")
        time.sleep(2)
        lackey.click("bt_tools.png")
        lackey.click("bt_profiler.png")
        result2 = lackey.exists("icon_info_profiler.png")
        lackey.click("bt_view_extended.png")
        lackey.click("bt_start.png")
        time.sleep(2)
        data_generator()
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
        assert result2 != None
    lackey.click("icon_connected.png")
        

