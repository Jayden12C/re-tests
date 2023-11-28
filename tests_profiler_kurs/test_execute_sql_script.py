import lackey
from re_tests_plugin import *
import time
import os
import platform
from lackey.InputEmulation import Mouse

text_file = """ 

CREATE TABLE Employee  ( 
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary DECIMAL(10, 2)
); 

INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary) 
VALUES (1, 'John', 'Doe', 50000.00);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary) 
VALUES (2, 'Jane', 'Smith', 60000.00);

SELECT * FROM Employee; 

UPDATE Employee 
SET Salary = 55000.00

WHERE EmployeeID = 1;

DELETE FROM Employee WHERE EmployeeID = 2;
"""
#Тест sql script из файла с инструментом профайлер
def test_execute_sql_script1():
    #Перед началом теста укажите в тесте и в Red Expert где будет папка test_script.txt
    current_os = platform.system()
    if current_os == "Windows":
        file_path = 'D:\\study\\Leto\\re-tests\\files\\test_script.txt'
        file = open(file_path, 'w')
        file.write(text_file)
        file.close()
    elif current_os == "Linux":
        file_path = "/var/lib/test_script.txt"
        file = open(file_path, 'w')
        file.write(text_file)
        file.close()
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
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("bt_execute_sql_script.png")
    result2 = lackey.exists("icon_execute_sql.png")
    lackey.click("bt_use_connections.png")
    lackey.click("bt_browse2.png")
    lackey.doubleClick("txt_file_sql.png")
    time.sleep(3)
    lackey.click("bt_bigstart.png")
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(5)
    lackey.click("tab_query_editor.png")
    lackey.type("DROP TABLE EMPLOYEE;")
    lackey.click("icon_execute_query.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.rightClick("icon_tab_profiler.png")
    lackey.click("bt_tab_close_all.png")
    lackey.doubleClick("icon_connected.png")
    distance = 30
    mouse_controller = Mouse()
    current_position = mouse_controller.getPos()
    new_position = current_position.offset(distance,0)
    mouse_controller.move(new_position)
    assert result1 != None
    assert result2 != None

def test_execute_sql_script2():
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
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    lackey.type(text_file)
    lackey.click("bt_format_sql.png")
    lackey.type(lackey.Key.F10)
    time.sleep(7)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(5)
    lackey.click("bt_discard.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("DROP TABLE EMPLOYEE;")
    lackey.click("icon_execute_query.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.rightClick("icon_tab_profiler.png")
    lackey.click("bt_tab_close_all.png")
    lackey.doubleClick("icon_connected.png")
    assert result1 != None
