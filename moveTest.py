import pyautogui

mouse_x, mouse_y = pyautogui.position()


x1 = mouse_x - 20
y1 = mouse_y + 20

print(mouse_x)
print(mouse_y)

pyautogui.moveTo(mouse_x,mouse_y)
pyautogui.moveTo(x1,y1,duration=1)
pyautogui.moveTo(x1,x1-100,duration=1)
pyautogui.moveTo(x1,y1+100,duration=1)
