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
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)    #waiting time to open connection
    lackey.click("icon_conn_open.png")
    #actions after test:
    yield
    lackey.doubleClick("icon_conn_open.png")
    
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
