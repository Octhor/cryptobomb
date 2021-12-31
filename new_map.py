import pyautogui
import time

starter = int(0)
time.sleep(2)

#Main
def new_map():
    #Connect Wallet Button click
    if pyautogui.locateOnScreen('newmap_button.jpg', grayscale=True, confidence=0.8) != None:
        newmap__button = pyautogui.locateOnScreen('newmap_button.jpg', confidence=0.8)
        newmap_Button_x, newmap_Button_y = pyautogui.center(newmap__button)
        print("New map found, changing maps.")
        pyautogui.click(newmap_Button_x, newmap_Button_y)
        pyautogui.click(newmap_Button_x, newmap_Button_y)
        time.sleep(3)
