import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_1(open_connection):
    with fdb.connect(database='localhost:employee', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        cur = con.cursor()
        cur.execute('CREATE USER "DEMO" PASSWORD \'pass\'')
        cur.execute('CREATE USER "dEmO" PASSWORD \'pass\'')
        con.commit()
        cur.close()
    
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_users.png")
    lackey.click("tree_reload_menu.png")
    all_plus = lackey.findAll("tree_plus.png")
    lackey.click(list(all_plus)[8])
    lackey.rightClick("tree_user_name1.png")
    lackey.click("tree_edit_menu.png")
    lackey.click("tab_SQL.png")
    result1 = lackey.find("sql_text_user1.png")
    lackey.click("bt_OK.png")
    lackey.rightClick("tree_user_name2.png")
    lackey.click("tree_edit_menu.png")
    lackey.click("tab_SQL.png")
    result2 = lackey.find("sql_text_user2.png")
    lackey.click("bt_OK.png")

    with fdb.connect(database='localhost:employee', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        cur = con.cursor()
        cur.execute('DROP USER "DEMO"')
        cur.execute('DROP USER "dEmO"')
        con.commit()
        cur.close()

    assert result1 != None
    assert result2 != None