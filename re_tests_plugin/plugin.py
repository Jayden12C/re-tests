import pytest
import lackey
import time
import platform


ADMIN_NAME = 'sysdba'
ADMIN_PASSWORD = 'masterkey'

@pytest.fixture()
def open_connection():
    #actions befor test:
    lackey.App.focus("Red Expert")
    if lackey.exists("tree_name_of_conn_blue.png") != None:
        lackey.doubleClick("tree_name_of_conn_blue.png")
    else:
        lackey.doubleClick("tree_name_of_conn.png")
    time.sleep(2)    #waiting time to open connection
    lackey.click("tree_name_of_open_conn_blue.png")
    #actions after test:
    yield
    if lackey.exists("tree_name_of_open_conn.png") != None:
        lackey.doubleClick("tree_name_of_open_conn.png")
    else:
        lackey.doubleClick("tree_name_of_open_conn_blue.png")
    
@pytest.fixture(scope='session', autouse=True)
def create_connection():
    lackey.App.focus("Red Expert")
    
    image_path = ["files/images/"]

    #code for the future
    # if platform.system() == "Windows":
    #     image_path += ["Windows/"]
    # else:
    #     image_path += ["Linux/"]
    
    lackey.SettingsMaster.ImagePaths = image_path
    lackey.SettingsMaster.MinSimilarity = 0.97