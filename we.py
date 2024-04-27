import pyautogui
import time
import webbrowser

webbrowser.open("https://www.youtube.com/@T-Tech253")
time.sleep(18)
screen_width, screen_height = pyautogui.size()

subscribe_button_x = 500
subscribe_button_y = 450
pyautogui.moveTo(subscribe_button_x, subscribe_button_y, duration=1)
pyautogui.click()
pyautogui.click()
xy=500
yx=495
pyautogui.moveTo(xy,yx,duration=1)
pyautogui.click()