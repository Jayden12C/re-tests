import lackey
from re_tests_plugin import *

def test_1():
    lackey.click("str_menu_database.png")
    lackey.click("str_menu_generate_erd.png")
    lackey.click("str_menu_create_new_erd.png")
    result1 = lackey.exists("grid_cell.png")
    lackey.rightClick("grid_cell.png")
    y = lackey.exists("erd_view_menu.png").getTarget().getY()   
    lackey.click("erd_view_menu.png")
    x = lackey.exists("chb_erd_display_grid_menu.png").getTarget().getX()
    mouse = lackey.Mouse()
    mouse.move(loc=lackey.Location(x, y))
    lackey.click("chb_erd_display_grid_menu.png")
    result2 = lackey.exists("grid_cell.png")
    lackey.rightClick("tab_erd_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 == None
