import tkinter as tk
import pyautogui
import time
import win32gui
from tkinter import messagebox

window = tk.Tk()
window.title('hbs')
window.geometry('600x600+100+100')
window.resizable(False,False)


cursor_type = win32gui.GetCursorInfo()

x = 0
y = 0

confidence_threshold = 0.5 # 이미지 분석 정확도
start_time = time.time()  # 시작 시간 저장
time_limit = 2  # 제한 시간 설정 (예: 10초)

def mouse1():
    time.sleep(2)
    global x,y
    a = pyautogui.position()
    x = a[0]
    y = a[1]

mouse1() #마우스 최초위치 설정

pyautogui.moveTo(x,y) #마우스 최초위치로 이동

#이미지 찾기 범위 지정
mouse_x, mouse_y = pyautogui.position()
global region_x1,region_y1
region_x1 = mouse_x - 20
region_y1 = mouse_y + 20

print(mouse_x,mouse_y)
print('region_x1',region_x1)
print('region_y1',region_y1)

#click event start!
for i in range(20):
    #이미지 위치 찾아서 img1에 저장
    img1 = pyautogui.locateCenterOnScreen('./img/heart.png',region=(mouse_x,mouse_y,1920,300))
    
    #이미지 위치를 못찾았을 경우
    while img1 is None:
        pyautogui.scroll(10)
        img1 = pyautogui.locateOnScreen('./img/heart.png', confidence=0.8,region=(x,y,1920,300))
        if img1 is not None:
            break
    
    #img1을 찾았을 경우 img1의 위치로 이동
    pyautogui.moveTo(img1)
    pyautogui.click()


    img2 = pyautogui.locateCenterOnScreen('./img/emotion.png',confidence=0.9,region=(mouse_x,mouse_y,1920,300))

    #이모티콘을 못찾았을 경우 찾을 때까지 반복
    while img2 is None:
        img2 = pyautogui.locateCenterOnScreen('./img/emotion.png',confidence=0.9,region=(mouse_x,mouse_y,1920,300))

    pyautogui.click(img2)
    pyautogui.click(img1)
    pyautogui.moveTo(img2)
    pyautogui.move(-40,0)
    pyautogui.click()
    pyautogui.moveTo(x,y)
    pyautogui.scroll(25)

    print(i,'번째 반복문 종료')
    # window.mainloop()