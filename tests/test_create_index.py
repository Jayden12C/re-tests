import lackey
from re_tests_plugin import *


def create_index():
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_indices.png")
    lackey.click("tree_create_menu.png")


def test_check_default_active(open_connection):
    create_index()
    result = lackey.exists("chb_active.png")
    lackey.click("bt_cancel.png")
    assert result != None


def test_check_order_fields(open_connection):
    create_index()
    lackey.click("cmb_name_table_COUNTRY.png")
    lackey.click("table_name_EMPLOYEE.png")
    lackey.click("bt_dbl_triangle_left.png")
    lackey.click("column_name_EMP_NO.png")
    for _ in range(5):
        lackey.click("bt_sngl_triangle_down.png")
    result = lackey.exists("index_selected_columns_after_5.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result != None