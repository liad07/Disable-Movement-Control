import pyautogui
import keyboard
import sys

def disapeer_all():
    import pygetwindow as gw

    # Get a list of all open windows
    windows = gw.getAllWindows()

    # Minimize all open windows
    for window in windows:
        window.minimize()


def block_all_keys():
    supported_keys = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'space', 'enter', 'esc', 'tab', 'backspace', 'insert', 'delete',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10',
        'f11', 'f12',
        'up', 'down', 'left', 'right',
        'shift', 'ctrl', 'alt', 'win']

    for key in supported_keys:
        keyboard.block_key(key)




# Disable mouse movement
pyautogui.FAILSAFE = False
disapeer_all()
block_all_keys()
pyautogui.moveTo(-100, -100)

# Continuously move the mouse to the same position to "disable" it
while True:

    pyautogui.moveTo(-100, -100, duration=0.1)

    # Check if the "Esc" key has been pressed
    if keyboard.is_pressed('esc'):
        sys.exit()  # Exit the entire program