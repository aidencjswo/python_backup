from tkinter import*
import tkinter
import pyautogui
import time;
import pyperclip

x1 = 0
y1 = 0  
x2 = 0
y2 = 0
#반복문
i = 0
time1 = 0

window=tkinter.Tk()


a = []

def mousePosition1():
    global x1, y1
    time.sleep(2)
    a = pyautogui.position()
    x1 = a[0]
    y1 = a[1]
    string_bar1.set("첫번 째 마우스 위치는 : "+"x:"+str(x1)+", y:"+str(y1))
    
def mousePosition2():
    global x2,y2
    time.sleep(2)
    a = pyautogui.position()
    print(x1,y1)
    x2 = a[0]
    y2 = a[1]
    string_bar2.set("두번 째 마우스 위치는 : "+"x:"+str(x2)+", y:"+str(y2))    


def moveMouse():
    global i
    i = spinBox.get()
    print(x1,y1)
    pyautogui.moveTo(x1,y1)
    pyautogui.click()
    pyautogui.moveTo(x2,y2)
    for i in range(int(i)):
        pyautogui.doubleClick()
        time.sleep(0.5)

def chatWrite():
    pyperclip.copy('금요일에 뭐 먹고싶음 질문')
    for i in range():
        pyautogui.moveTo(x1,y1)
        pyautogui.click()
        pyautogui.hotkey('ctrl','v')
        pyautogui.write(str(i+1))       
        pyautogui.moveTo(x2,y2)
        pyautogui.click()


window.title("카카오톡이모티콘보내기")
window.geometry("640x400+100+100")
window.resizable(False,False)

spinBox = tkinter.Spinbox(window,from_=0,to=50,width=5)
spinBox.pack()

button1 = tkinter.Button(window,text='마우스위치설정1(2초 후 설정)',command=mousePosition1,background = 'white')
button1.pack()
#동적 변수 할당을 위한 StringVar() 선언
string_bar1=tkinter.StringVar()
string_bar2=tkinter.StringVar()

label1 = tkinter.Label(window, textvariable=string_bar1)
label1.pack()
button2 = tkinter.Button(window,text='마우스위치설정2',command=mousePosition2,background = 'white')
button2.pack()
label2 = tkinter.Label(window, textvariable=string_bar2)
label2.pack()
button3 = tkinter.Button(window,text='폭탄투하',command=moveMouse,background= 'red')
button3.pack()
button4 = tkinter.Button(window,text='글씨쓰기',command=chatWrite)
button4.pack()

input_text = Entry(window, width=30)
# button5 = tkinter.Button(window,text='글씨복사하기',command=confirm)
# button5.pack()
input_text.pack()

window.mainloop()


# pyautogui.click()
# pyautogui.moveTo(900,328)
# pyautogui.click()
# for i in range(100):
#     pyautogui.click()
