import pyautogui
import os
import pytest
import time

def test_open_connection():
    current_directory = os.getcwd()
    
    init_re = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/init_re.png"))
    pyautogui.click(init_re)
    
    init_br_bd = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/init_br_bd.png"))
    pyautogui.click(init_br_bd)

    b_new_conn = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/b_new_connection.png"))
    pyautogui.click(b_new_conn)
    
    t_file_bd = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/t_file_bd.png"))
    pyautogui.click(t_file_bd)
    pyautogui.write("employee.fdb")

    t_user_name = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/t_user_name.png"))
    pyautogui.click(t_user_name)
    pyautogui.write("sysdba")

    t_user_password = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/t_user_password.png"))
    pyautogui.click(t_user_password)
    pyautogui.write("masterkey")

    b_test = pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/b_test.png"))
    pyautogui.click(b_test)

    is_open_conn = False

    for _ in range(5):
        if pyautogui.locateCenterOnScreen(os.path.join(current_directory, "files/images/m_connection_true.png")) != None:
            is_open_conn = True
            pyautogui.press('enter')
            return
        else:
            time.sleep(1)

    assert is_open_conn == True