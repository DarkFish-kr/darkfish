 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/random_mouse.py b/random_mouse.py
new file mode 100644
index 0000000000000000000000000000000000000000..8525edf07ae798c71d251d3c233895f6cf7dd24b
--- /dev/null
+++ b/random_mouse.py
@@ -0,0 +1,28 @@
+"""Randomly move the mouse within the screen and click using pyautogui."""
+import random  # Built-in module for generating random numbers.
+import time  # Built-in module to pause execution between actions.
+
+import pyautogui  # Library that controls the mouse and keyboard.
+
+pyautogui.FAILSAFE = True  # Moving the mouse to a corner stops the script for safety.
+SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()  # Get screen size to keep coordinates in bounds.
+
+
+def random_point() -> tuple[int, int]:
+    """Return a random (x, y) coordinate within the current screen."""
+    x = random.randint(0, SCREEN_WIDTH - 1)  # Pick a random horizontal position.
+    y = random.randint(0, SCREEN_HEIGHT - 1)  # Pick a random vertical position.
+    return x, y  # Give back the coordinate pair.
+
+
+def random_move_and_click(count: int = 5, move_duration: float = 0.5, pause_between: float = 0.8) -> None:
+    """Move to random points and click them a set number of times."""
+    for _ in range(count):  # Repeat for the desired number of clicks.
+        target_x, target_y = random_point()  # Choose a fresh random target.
+        pyautogui.moveTo(target_x, target_y, duration=move_duration)  # Glide the mouse to the target.
+        pyautogui.click()  # Perform a left click at the target location.
+        time.sleep(pause_between)  # Pause to mimic human pacing and avoid rapid clicks.
+
+
+if __name__ == "__main__":  # Run this block only when executing the script directly.
+    random_move_and_click(count=10, move_duration=0.4, pause_between=1.0)  # Start with sensible defaults.
 
EOF
)
