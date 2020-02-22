import keyboard
import pyautogui
import time
import os
from os import getenv


# keyboard.all_modifiers = {'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 
# 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}

midi_file_path = input("Please enter file path (including the file name) for the MIDI file:\n") 
# 
# print(os.environ)
# print(getenv("GP5_FILE_LOCATION"))

keyboard.press_and_release('left windows + r')
time.sleep(2)
keyboard.write(getenv("GP5_file_location"), delay=0.02)
keyboard.press_and_release('enter')
time.sleep(10)
keyboard.press_and_release('ctrl + o')
keyboard.write(midi_file_path)
keyboard.press_and_release('enter')
time.sleep(2)

pyautogui.press('tab', presses=5) # select "import"
keyboard.press_and_release('enter')

# Mouse click on the "import" window --> "alt + c" to close the window

# Press "alt" and select "Track" with the arrow keys


'''
# Examples
print(pyautogui.size()) # screen resolution
width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position()) # current position of the mouse pointer

pyautogui.moveTo(10, 10) # moves the mouse pointer immediately
pyautogui.moveTo(1000, 1000, duration = 1) # moves mouse pointer slower (duration = in seconds)
pyautogui.moveRel(200, 0, duration = 1) # x and yOffset, moves from current position in x or y direction, 0 pixels
pyautogui.moveRel(0, -600, duration = 1) # y-axis decreases in the upwards direction, we need a negative number relatively
print(pyautogui.position())

#dragTo and dragRel are used to drag the mouse position

pyautogui.click(330,120)
# also: pyautogui.middleClick(), doubleClick(), rightClick()

pyautogui.press('tab', presses=5)
time.sleep(1)
keyboard.press_and_release('alt')
keyboard.press_and_release('ctrl + l')
keyboard.write("file_path_here", delay=0.02)
'''