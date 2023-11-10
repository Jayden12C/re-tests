import lackey
from re_tests_plugin import *
import time

def test_grand_manager(open_connection):
    lackey.click("bt_tools.png")
    lackey.click("bt_profiler.png")
    result1 = lackey.exists("icon_info_profiler.png")
    lackey.click("bt_view_extended.png")
    lackey.click("bt_start.png")
    lackey.click("bt_grand_manager.png")
    result2 = lackey.exists("icon_grand_manager.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)
    lackey.click("bt_resume.png")
    lackey.click("bt_icon_grand_manager.png")
    lackey.click("bt_system_object_show.png")
    time.sleep(2)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_pause.png")
    time.sleep(3)
    lackey.click("bt_resume.png")
    lackey.click("bt_icon_grand_manager.png")
    lackey.click("icon_public.png")
    time.sleep(3)
    lackey.click("icon_tab_profiler.png")
    lackey.click("bt_stop.png")
    time.sleep(4)
    lackey.rightClick("icon_info_profiler.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None