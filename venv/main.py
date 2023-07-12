import pyautogui
import random
import time

pyautogui.size()

def press_random_key():
    key = random.choice(['w', 'a', 's', 'd'])
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

while True:
    time.sleep(5)
    if pyautogui.locateCenterOnScreen('rust_bag.png',grayscale=True, confidence=.5) == None:
            x = random.randint(600, 900)
            press_random_key()
            time.sleep(1)
            press_random_key()
            time.sleep(x)
    else:
        click = pyautogui.locateCenterOnScreen('rust_bag.png',grayscale=True, confidence=.5)
        pyautogui.doubleClick(click)
        time.sleep(1)
