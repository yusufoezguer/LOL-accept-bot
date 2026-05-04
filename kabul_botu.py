import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time

while True:
    kabul = imagesearch("./buton.png")
    if kabul[0] != -1:
        pyautogui.leftClick(kabul[0]+142 , kabul[1]+39)
        time.sleep(13)


