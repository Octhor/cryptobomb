import pyautogui
import time

starter = int(0)
time.sleep(2)
error = False
#Main
def error():
    #Connect Wallet Button click
    if pyautogui.locateOnScreen('error.jpg', grayscale=True, confidence=0.8) != None:
        return True
    elif pyautogui.locateOnScreen('connect_wallet_button.jpg', grayscale=True, confidence=0.75) != None:
        return True
    else:
        return False
