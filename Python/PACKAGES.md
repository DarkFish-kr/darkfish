 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/PACKAGES.md b/PACKAGES.md
new file mode 100644
index 0000000000000000000000000000000000000000..dabc8f8f4c74def9755ab38b8d0fce61b59eafbe
--- /dev/null
+++ b/PACKAGES.md
@@ -0,0 +1,41 @@
+# Python Packages for Random Mouse Movement and Clicking
+
+Below are commonly used packages for automating mouse movement and clicks in Python. Each option can move the cursor to random positions, perform clicks, and add delays to mimic human interaction.
+
+## 1. `pyautogui`
+- **Strengths:** Cross-platform (Windows, macOS, Linux), simple API for moving the mouse, clicking, scrolling, and capturing screenshots.
+- **Features:** `moveTo`, `moveRel`, `click`, `dragTo`, `position`, and fail-safe hotkey (Ctrl+C or moving the mouse to a corner).
+- **When to use:** General-purpose desktop automation and GUI scripting.
+
+### Frequently used `pyautogui` functions (10)
+- `size()`: Returns the screen resolution so you can randomize coordinates safely within bounds.
+- `position()`: Reads the current mouse coordinates; useful for debugging target locations.
+- `moveTo(x, y, duration=0)`: Moves the mouse to absolute screen coordinates, optionally over a duration.
+- `moveRel(xOffset, yOffset, duration=0)`: Moves the mouse relative to its current position.
+- `click(x=None, y=None, button="left")`: Clicks (defaults to left) at the current or given coordinates.
+- `doubleClick(x=None, y=None, button="left")`: Performs a double-click.
+- `rightClick(x=None, y=None)`: Convenience helper for right-clicks.
+- `scroll(clicks, x=None, y=None)`: Scrolls vertically from the current or specified position.
+- `dragTo(x, y, duration=0, button="left")`: Drags the mouse to absolute coordinates while holding the specified button.
+- `typewrite(message, interval=0.0)`: Types text with an optional delay between keystrokes for more human-like input.
+
+## 2. `pynput`
+- **Strengths:** Fine-grained control of mouse and keyboard input with event listeners.
+- **Features:** `Controller` for moving/clicking, listeners for responding to system input, supports relative and absolute movement.
+- **When to use:** When you need both automation and the ability to react to user input.
+
+## 3. `autopy`
+- **Strengths:** Lightweight and fast for mouse/keyboard control and screenshots.
+- **Features:** `mouse.move`, `mouse.click`, `screen.size` for screen bounds, random coordinate generation is straightforward.
+- **When to use:** Low-dependency alternative when you want speed over extensive convenience functions.
+
+## 4. `opencv-python` (optional helper)
+- **Strengths:** Computer-vision helper for locating UI elements or regions before moving/clicking.
+- **Features:** Template matching (`cv2.matchTemplate`), color detection, and coordinate extraction that can be paired with any mouse-control library.
+- **When to use:** When clicks need to target dynamic or image-defined locations.
+
+## Usage Tips
+- Use `random` to generate coordinates within `pyautogui.size()` or `autopy.screen.size()` bounds before calling move/click functions.
+- Add `time.sleep()` between moves and clicks to feel more human and to avoid overwhelming the system.
+- On Linux systems without a display (e.g., headless servers), a virtual display (Xvfb) may be required for GUI automation.
+- Always test with small scripts first and keep an emergency stop key (e.g., `pyautogui.FAILSAFE = True`).
 
EOF
)
