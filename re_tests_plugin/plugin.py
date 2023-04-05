import pytest
import lackey
import time

@pytest.fixture()
def open_connection():
    #actions befor test:
    lackey.App.focus("Red Expert")
    if lackey.exists("files/images/tree_name_of_conn_blue.png") != None:
        lackey.doubleClick("files/images/tree_name_of_conn_blue.png")
    else:
        lackey.doubleClick("files/images/tree_name_of_conn.png")
    time.sleep(5)    #waiting time to open connection
    #actions after test:
    yield
    lackey.doubleClick("files/images/tree_name_of_open_conn.png")
    
# @pytest.fixture(scope='session', autouse=True)
# def create_connection():
#     pass   