import tkinter
import pyautogui
import win32gui
import time

time.sleep(2)

# 커서 상태 확인
cursor_info = win32gui.GetCursorInfo()
cursor = cursor_info[1]
print(cursor)

# 커서가 텍스트 커서(32512)가 아닌 동안 스크롤 진행
while cursor != 65543:
    pyautogui.scroll(10)
    cursor_info = win32gui.GetCursorInfo()
    cursor = cursor_info[1]
