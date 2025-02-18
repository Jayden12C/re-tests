from lackey.InputEmulation import Mouse
import lackey
from re_tests_plugin import *
import time
import os
import platform


def test_add_database():
    mouse = Mouse()
    direction = Mouse.WHEEL_DOWN
    steps = 9
    lackey.click("bt_create_new_connection.png")
    time.sleep(2)
    lackey.click("icon_character.png")
    location = lackey.find("icon_character_open.png")
    if location:
        mouse.move(location.getCenter())
    mouse.wheel(direction, steps)
    lackey.click("UTF.png")
    lackey.click("conection_name.png")
    lackey.type("Test_kurs")
    lackey.click("data_base_file.png")
    lackey.type("test_kurs")
    lackey.click("user_name.png")
    lackey.type("sysdba")
    lackey.click("password.png")
    lackey.type("masterkey")
    lackey.click("bt_create.png")
    result2 = lackey.exists("register_database.png")
    lackey.click("bt_yes.png")
    time.sleep(2)
    result3 = lackey.exists("icon_phone_test_clicked.png")
    assert result2 != None
    assert result3 != None


def test_add_tables():
    if lackey.exists("icon_phone_test.png"):
        lackey.click("icon_phone_test.png")
        lackey.click("icon_disconnected.png")
    elif lackey.exists("icon_phone_test_clicked.png"):
        lackey.click("icon_disconnected.png")
    else:
        pass

    result2 = lackey.exists("tab_query_editor_text.png")
    create_table_sql1 = """CREATE TABLE PHONE (ID_PHONE INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "NAME" VARCHAR(10), "NUMBER" INTEGER NOT NULL, CONSTRAINT PK_PHONE_1 PRIMARY KEY (ID_PHONE)); """
    lackey.type(create_table_sql1)
    lackey.click("bt_format_sql.png")
    result3 = lackey.exists("create_table1.png")
    lackey.click("icon_execute_query.png")
    result4 = lackey.exists("table_create1.png")
    time.sleep(2)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    create_table_sql2 = """CREATE TABLE OPERATOR (ID_OPERATOR INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL,ID_PHONE INTEGER NOT NULL,"NAME" VARCHAR(10) NOT NULL,"NUMBER" INTEGER NOT NULL,CONSTRAINT PK_OPERATOR_1 PRIMARY KEY (ID_OPERATOR),CONSTRAINT FK_OPERATOR_1 FOREIGN KEY (ID_PHONE) REFERENCES PHONE (ID_PHONE));"""
    lackey.type(create_table_sql2)
    lackey.click("bt_format_sql.png")
    result5 = lackey.exists("create_table2.png")
    lackey.click("icon_execute_query.png")
    result6 = lackey.exists("table_create2.png")
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("""INSERT INTO PHONE ("NAME", "NUMBER")
VALUES ('Jene', 12345);""")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)
    lackey.click("bt_resume.png")
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("""INSERT INTO OPERATOR (ID_PHONE, "NAME", "NUMBER")
VALUES (1, 'Tele2', 111);""")
    lackey.click("icon_execute_query.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(3)
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("""SELECT
    PHONE."NAME" AS PhoneName,
    OPERATOR."NAME" AS OperatorName,
    PHONE."NUMBER" AS PhoneNumber,
    OPERATOR."NUMBER" AS OperatorNumber FROM PHONE JOIN OPERATOR ON PHONE.ID_PHONE = OPERATOR.ID_PHONE;""")
    lackey.click("bt_format_sql.png")
    lackey.click("bt_execute_profiler.png")
    time.sleep(3)
    lackey.click("tab_query_editor.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.rightClick("tab_query_editor.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None
    assert result6 != None


def test_remove_connected_test_kurs():
    time.sleep(2)
    if lackey.exists("icon_phone_test_clicked.png"):
        lackey.click("bt_remove.png")
        lackey.click("bt_yes.png")
    elif lackey.exists("icon_phone_test.png"):
        lackey.click("bt_remove.png")
        lackey.click("bt_yes.png")
    else:
        pass
    time.sleep(2)
    current_os = platform.system()
    if current_os == "Windows":
        file_path = "C:\\Windows\\System32\\TEST_KURS"
        os.remove(file_path)
    elif current_os == "Linux":
        linux_file_path = "/var/lib/test_kurs"
        os.remove(linux_file_path)




