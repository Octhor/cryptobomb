from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
import win32api, win32con, win32gui
from get_window import WindowMgr
import automation
import new_map
import error
import set_window
import pygetwindow as gw #USED TO MINIMIZE WINDOWS AND SO ON


## Used to get all windows titles
# all_titles = gw.getAllTitles()
# print(all_titles)

#Titles of the browsers of each account
Pessoal = gw.getWindowsWithTitle('bombcrypto - Pessoal — Microsoft\u200b Edge')[0]
Conta_1 = gw.getWindowsWithTitle('bombcrypto - Conta 1 — Microsoft\u200b Edge')[0]
Conta_2 = gw.getWindowsWithTitle('bombcrypto - Conta 2 — Microsoft\u200b Edge')[0]
Conta_3 = gw.getWindowsWithTitle('bombcrypto - Conta 3 — Microsoft\u200b Edge')[0]
Conta_4 = gw.getWindowsWithTitle('bombcrypto - Conta 4 — Microsoft\u200b Edge')[0]
Conta_5 = gw.getWindowsWithTitle('bombcrypto - Conta 5 — Microsoft\u200b Edge')[0]

def minimize_browser():
    Pessoal.minimize()
    Conta_1.minimize()
    Conta_2.minimize()
    Conta_3.minimize()
    Conta_4.minimize()
    Conta_5.minimize()

def max_browser():
    Pessoal.restore()
    Conta_1.restore()
    Conta_2.restore()
    Conta_3.restore()
    Conta_4.restore()
    Conta_5.restore()

starter = int(0)
time.sleep(1)


#The code is called for two browsers, based on the "name" of the window. Change it if needed
#The script works based in images, so if your screen is different, take new prints for each image.

def f5():
    #reload page to start the loop
    #pyautogui.keyDown('ctrl') #un-comment this if you need hard-reset
    pyautogui.keyDown('f5')
    time.sleep(0.1)
    #pyautogui.keyUp('ctrl')
    pyautogui.keyUp('f5')
    time.sleep(5) #increase this if your connnection takes more than 7 sec to load the button

def routine(browser):
        minimize_browser()
        browser.maximize()
        set_window.set_browser(browser)
        time.sleep(0.7)
        #Reload the page
        f5()
        automation.automation()
        browser.restore()

def menu(browser):
    minimize_browser()
    browser.maximize()
    set_window.set_browser(browser)
    time.sleep(0.5)
    automation.back_to_menu()
    browser.restore()


def main():
    while keyboard.is_pressed('q') == False and starter == 0:
#minimize all browsers
        

        routine(Pessoal)
        routine(Conta_1)
        routine(Conta_2)
        routine(Conta_3)
        routine(Conta_4)
        routine(Conta_5)
        max_browser()

        if error.error() == True:
            #Trying to find error on the screen after completing the run if true, run again
            print("Error found on the screen, maybe because of the server. Running again in 5s")
            time.sleep(5)
            main()
        else:
            print("No error was found, continuing.")
            #system to get to a new map
            #Wait one hour to rerun and make everyone go to work again
            for i in range(10):
                #Search if the map is finished > change map
                new_map.new_map()

                #Search for errors
                if error.error() == True:
                    print("Found 'error on the screen, restarting the run")
                    main()
                else:
                    time.sleep(randint(240, 300))
                    new_map.new_map()
                    menu(Pessoal)
                    new_map.new_map()
                    menu(Conta_1)
                    new_map.new_map()
                    menu(Conta_2)
                    new_map.new_map()
                    menu(Conta_3)
                    new_map.new_map()
                    menu(Conta_4)
                    new_map.new_map()
                    menu(Conta_5)
                    max_browser()
                
            main()
main()