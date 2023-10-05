import lackey
import time
from re_tests_plugin import *

def test_1(open_connection):
    lackey.SettingsMaster.MinSimilarity = 0.7
    move_location = lackey.find("icon_connected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    result = lackey.exists("hint_disconnect.png")
    lackey.SettingsMaster.MinSimilarity = 0.97
    assert result != None

def test_2():
    lackey.SettingsMaster.MinSimilarity = 0.7
    move_location = lackey.find("icon_disconnected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    result = lackey.exists("hint_connect.png")
    lackey.SettingsMaster.MinSimilarity = 0.97
    assert result != None