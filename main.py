import time
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
STOP_KEY = "alt"
CPS = 100
DELAY = 5

for i in range(DELAY):
    print(f"{DELAY - i} ", end="")
    time.sleep(1)
print(f"\nPress [{STOP_KEY.upper()}] to end script.")

while not keyboard.is_pressed(STOP_KEY):
    mouse.press(Button.left)
    time.sleep(1 / (CPS*2))
    mouse.release(Button.left)
    time.sleep(1 / (CPS*2))
