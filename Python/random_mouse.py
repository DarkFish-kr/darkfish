import pyautogui
import random
import time

screenWidth, screenHeight = pyautogui.size()

for i in range(5):
    randomX = random.randint(0, screenWidth)
    randomY = random.randint(0, screenHeight)
    pyautogui.moveTo(randomX, randomY, duration=1)
    pyautogui.click()
    time.sleep(1)