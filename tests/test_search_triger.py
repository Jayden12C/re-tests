import time
import lackey
from re_tests_plugin import *


def test_search_triger(open_connection):
    triger = "alter trigger fts$trig_22 sql security definer"
    lackey.click("tree_plus.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type(triger)
    lackey.click("icon_execute_query.png")
    time.sleep(5)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.DELETE)
    lackey.type("s", lackey.Key.CTRL)