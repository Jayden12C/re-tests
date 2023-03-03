import os
import pytest
import time
import lackey

def test_open_connection():
	time.sleep(600)
	lackey.App.focus("Red Expert")
	lackey.click("files/images/init_db_browser.png")
	lackey.click("files/images/bt_new_conn.png")
	lackey.click("files/images/text_input_db.png")
	lackey.type("employee.fdb")
	lackey.click("files/images/text_input_user.png")
	lackey.type("sysdba")
	lackey.click("files/images/text_input_password.png")
	lackey.type("masterkey")
	lackey.click("files/images/bt_test.png")
	lackey.wait("files/images/ms_test_ok.png", 5)
	
	assert lackey.exists("files/images/ms_test_ok.png") != None, "Lackey dont find pattern"
