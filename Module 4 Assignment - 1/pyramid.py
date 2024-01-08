from time import sleep
import pyautogui
n = int(input())
sleep(10)
for i in range(1,n + 1):
    pyautogui.write('#' * i, interval=0.01)
    pyautogui.press('enter')