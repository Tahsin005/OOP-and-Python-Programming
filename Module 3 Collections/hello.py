import pyautogui
from time import sleep
sleep(10)
for i in range(1,501):
    pyautogui.write(f'{i}', interval=0.01)
    pyautogui.press('enter')
