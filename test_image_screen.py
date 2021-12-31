from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
import win32api, win32con, win32gui

starter = int(0)

def work(img,  gray,conf):
    try:
        while pyautogui.locateOnScreen(img, confidence=conf) is not None:
            Button = pyautogui.locateOnScreen(img, grayscale=gray, confidence=conf)
            Button_x, Button_y = pyautogui.center(Button)
            print(img, " Button position: X:", Button_x, "Y:", Button_y)
            pyautogui.click(Button_x, Button_y)
            time.sleep(10)
    except TypeError:
        print("Function failed to find ", img, " on the screen.")

work('sign_wallet_button.jpg', False, 0.80)