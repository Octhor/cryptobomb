import pyautogui
import time
import pygetwindow as gw #USED TO MINIMIZE WINDOWS AND SO ON


## Used to get all windows titles
# all_titles = gw.getAllTitles()
# print(all_titles)

#Titles of the browsers of each account
Pessoal = gw.getWindowsWithTitle('bombcrypto - Pessoal — Microsoft\u200b Edge')[0]
Pessoa_1 = gw.getWindowsWithTitle('bombcrypto - Pessoa 1 — Microsoft\u200b Edge')[0]
Conta_2 = gw.getWindowsWithTitle('bombcrypto - Conta 2 — Microsoft\u200b Edge')[0]

def minimize_browser():
    Pessoal.minimize()
    Pessoa_1.minimize()
    Conta_2.minimize()


def max_browser():
    Pessoal.restore()
    Pessoa_1.restore()
    Conta_2.restore()

