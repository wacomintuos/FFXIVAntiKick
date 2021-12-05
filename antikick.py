import time
import keyboard
import random
import win32api

from win32gui import GetWindowText, GetForegroundWindow

keypress = ['w', 'a', 's', 'd']

while (True):
    currentWindow = GetWindowText(GetForegroundWindow())

    if currentWindow == "FINAL FANTASY XIV":
        random_keypress = random.choice(keypress)
        keyboard.press_and_release(random_keypress)
        print('Pressed %s in %s' % (random_keypress, currentWindow))

    time.sleep(1)
