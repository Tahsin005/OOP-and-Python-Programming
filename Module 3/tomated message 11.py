import pyautogui
from time import sleep
sleep(10)
for i in range(1,20):
    pyautogui.write(f'Sending automated message {i}', interval=0.1)
    pyautogui.press('enter')

Sending automated message 1
Sending automated message 2
Sending automated message 3
Sending automated message 4
Sending automated message 5
Sending automated message 6
Sending automated messa
