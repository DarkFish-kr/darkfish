 # darkfish
-DarkFish
 
-made Data folder - 2025.11.27

\ No newline at end of file
+## Random mouse mover using pyautogui
+The repository includes `random_mouse.py`, a beginner-friendly script that moves the mouse to random on-screen points and clicks. Every line is commented so you can follow along while it runs.
+
+### How to run
+1. Install `pyautogui` (and, on Linux, ensure you have a GUI session):
+   ```bash
+   pip install pyautogui
+   ```
+2. Execute the script:
+   ```bash
+   python random_mouse.py
+   ```
+
+### What each part does
+- The imports pull in `random`, `time`, and `pyautogui` so you can generate coordinates, pause between clicks, and control the cursor.
+- `pyautogui.FAILSAFE = True` keeps an emergency stop available by moving the mouse to a screen corner.
+- `SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()` reads your screen size so coordinates stay inside the visible area.
+- `random_point()` returns a fresh `(x, y)` pair inside the screen bounds.
+- `random_move_and_click()` repeats a simple routine: pick a random point, glide there, click, and pause.
+- The `__main__` block starts the routine with 10 movements/clicks and pauses of about a second, which you can tweak for faster or slower pacing.
+
+Use `Ctrl+C` to stop the script at any time. Increase `count` for more clicks or adjust `move_duration`/`pause_between` to change the speed.
 
EOF
)
