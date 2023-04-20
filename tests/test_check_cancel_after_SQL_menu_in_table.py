import lackey
from re_tests_plugin import *

def action():
    lackey.click("tree_plus.png")
    all_plus = lackey.findAll("tree_plus.png")
    lackey.click(list(all_plus)[2])
    lackey.rightClick("tree_table_name_EMPLOYEE.png")
    move_location = lackey.find("tree_SQL_menu.png").getTarget()
    return move_location

def test_1(open_connection):
    move_location = action()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    lackey.click("tree_SELECT_SQL_menu.png")

    lackey.type("z", lackey.Key.CTRL)
    assert lackey.find("tab_query_editor_text.png") != None

def test_2(open_connection):
    move_location = action()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    lackey.click("tree_INSERT_SQL_menu.png")

    lackey.type("z", lackey.Key.CTRL)
    assert lackey.find("tab_query_editor_text.png") != None

def test_3(open_connection):
    move_location = action()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    lackey.click("tree_UPDATE_SQL_menu.png")

    lackey.type("z", lackey.Key.CTRL)
    assert lackey.find("tab_query_editor_text.png") != None

def test_4(open_connection):
    move_location = action()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    lackey.click("tree_CREATE_TABLE_SQL_menu.png")

    lackey.type("z", lackey.Key.CTRL)
    assert lackey.find("tab_query_editor_text.png") != None