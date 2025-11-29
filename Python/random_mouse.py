"""Randomly move ethe within the screen and click using pyautogui."""
import pyautogui
import random
import time

pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size()

def random_point() -> tuple[int, int]:
    """Return a random (x, y) coordinate within the screen dimensions."""
    x = random.randint(0, screenWidth - 1)
    y = random.randint(0, screenHeight - 1)
    return (x, y)

def random_move_and_click(count: int = 5, move_duration: float = 0.5, pause_between: float = 0.8) -> None:
    """Move to random points and click them a set number of times."""
    for _ in range(count):
        target_x, target_y = random_point()
        pyautogui.moveTo(target_x, target_y, duration=move_duration)
        pyautogui.click()
        time.sleep(pause_between)

if __name__ == "__main__":
    random_move_and_click(count=10, move_duration=0.4, pause_between=1.0)