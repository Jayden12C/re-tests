import time
import lackey
from re_tests_plugin import *


def test_search_trigger(open_connection):
    trigger = "alter trigger fts$trig_22 sql security definer"
    lackey.click("tab_query_editor_text.png")
    lackey.type(trigger)
    lackey.click("icon_execute_query.png")
    time.sleep(5)
    result = lackey.exists("Screenshot_red.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.DELETE)
    lackey.type("s", lackey.Key.CTRL)
    assert result != None