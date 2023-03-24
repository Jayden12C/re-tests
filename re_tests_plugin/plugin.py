import pytest
import lackey
import time

@pytest.fixture()
def open_connection():
    lackey.App.focus("Red Expert")
    lackey.rightClick("files/images/tree_name_of_conn_blue.png")
    lackey.click("files/images/tree_db_info.png")
    lackey.click("files/images/init_db_browser.png")
    lackey.click("files/images/bt_conn.png")
    while lackey.exists("files/images/tree_name_of_open_conn.png") == None:
        time.sleep(1)
    yield
    lackey.rightClick("files/images/tree_name_of_open_conn.png")
    lackey.click("files/images/tree_close_conn.png")
    
@pytest.fixture(scope='session', autouse=True)
def create_connection():
    lackey.App.focus("Red Expert")
    lackey.rightClick("files/images/tree_name_of_conn.png")
    lackey.click("files/images/tree_db_info.png")
    lackey.click("files/images/init_db_browser.png")
    lackey.click("files/images/text_input_db.png")
    lackey.type("employee.fdb")
    lackey.click("files/images/text_input_user.png")
    lackey.type("sysdba")
    lackey.click("files/images/text_input_password.png")
    lackey.type("masterkey")
    lackey.click("files/images/chb_store_pass.png")

    