from enum import auto
from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
import win32api, win32con, win32gui



starter = int(0)
#Function to screen in the heroes page in a human way, holding.
def move_mouse_clicked(x,y):
    for i in range(2):
        win32api.SetCursorPos((x-400,y))
        print("scrolling screen to the last hero")
        time.sleep(0.1)
        pyautogui.dragTo(x-400, y-340, 1, button='left')

#Using the upgrade button, get a position to scroll to the last active hero
def scroll(img, gray, conf):
    try:
        if pyautogui.locateOnScreen('upgrade_button.jpg', grayscale=True, confidence=0.7) is not None:
            Button = pyautogui.locateOnScreen('upgrade_button.jpg', confidence=0.7)
            Button_x, Button_y = pyautogui.center(Button)
            print(img, " Button position: X:", Button_x, "Y:", Button_y)
            move_mouse_clicked(Button_x, Button_y)
            time.sleep(2)
    except TypeError:
        print("Function failed to find ", img, " on the screen.")


def ImageSearch(img,  gray, conf):
    try:
        if pyautogui.locateOnScreen(img, grayscale=gray, confidence=conf) is not None:
            Button = pyautogui.locateOnScreen(img, grayscale=gray, confidence=conf)
            Button_x, Button_y = pyautogui.center(Button)
            print(img, " Button position: X:", Button_x, "Y:", Button_y)
            pyautogui.moveTo(Button_x, Button_y)
            time.sleep(0.1)
            pyautogui.click(Button_x, Button_y)
            pyautogui.click(Button_x, Button_y)
            time.sleep(1)
    except TypeError:
        print("Function failed to find ", img, " on the screen.")


def work(img,  gray, conf):
    try:
        while pyautogui.locateOnScreen(img, confidence=conf) is not None:
            Button = pyautogui.locateOnScreen(img, grayscale=gray, confidence=conf)
            Button_x, Button_y = pyautogui.center(Button)
            print(img, " Button position: X:", Button_x, "Y:", Button_y)
            pyautogui.click(Button_x, Button_y)
            time.sleep(1)
    except TypeError:
        print("Function failed to find ", img, " on the screen.")

def automation():
    #Find the "Connect Button"
    ImageSearch('connect_wallet_button.jpg', False, 0.55)
    time.sleep(3)

    #sign contract to connect
    ImageSearch('sign_wallet_button.jpg', False, 0.80)
    ImageSearch('sign2_wallet_button.jpg', False, 0.80)
    time.sleep(15)



    #Access the heroes page
    ImageSearch('heroes_button.jpg', True, 0.5)
    print("Image search Heroes")
    time.sleep(2)

    #Using the upgrade button, get a position to scroll to the last active hero
    scroll('upgrade_button.jpg', False, 0.75)
    time.sleep(1)

    #Search for the Work Button
    #For this part, the grayscale was removed, since the colors of active workers and innactive are pretty close
    work('work_button.jpg', False, 0.93)
    time.sleep(0.8)

    #Exit button ( Big Red X)
    ImageSearch('exit_button.jpg', True, 0.65)
    time.sleep(0.8)

    #Start the Treasure Hunt
    ImageSearch('treasure_button.jpg', False, 0.60)
    pyautogui.click()
    time.sleep(2)

def back_to_menu():

    ImageSearch('menu_arrow.jpg', False, 0.75)
    time.sleep(2)

    ImageSearch('treasure_button.jpg', False, 0.60)
    pyautogui.click()



