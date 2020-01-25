from tkinter import *
import math 
import time
global scvalue

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = scvalue.get()
                scvalue.set("error")
                screen.update()
                time.sleep(1)
        scvalue.set(value)
        screen.update()
    elif text == "√":
        scvalue.set(math.sqrt(float(scvalue.get())))
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "<":
        value = screen.get()
        new_value = value[0:-1]
        scvalue.set(new_value)
        screen.update()
    elif text == "ln":
        scvalue.set(math.log(float(scvalue.get())))
        screen.update()
    elif text == "sin":
        scvalue.set(math.sin(float(scvalue.get())))
        screen.update()
    elif text == "!":
        scvalue.set(math.factorial(int(scvalue.get())))
        screen.update()
    elif text == "cos":
        scvalue.set(math.cos(float(scvalue.get())))
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("360x770")
root.maxsize(360,770)
root.title("CALCULATOR")
objects = ['C','%','/','<','7','8','9','*','4','5','6','-','1','2','3','+','√','0','.','=','ln','sin','cos','!']
count = 0
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 50 bold", bg="black", fg="white")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
for i in range(5):
    f = Frame(root, bg="lightgrey")
    for j in range(4):
        b = Button(f, text=f"{objects[count]}", padx=4, pady=4, font="lucida 30 bold",borderwidth=10, relief=RAISED,bg="darkgrey", fg="black")
        b.pack(side= LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
        count += 1
    f.pack()
f = Frame(root, bg="lightgrey")
for i in range(4):
    b = Button(f, text=f"{objects[count]}", padx=4, pady=4, font="lucida 20 bold",borderwidth=10, relief=RAISED,bg="darkgrey", fg="black")
    b.pack(side= LEFT, padx=2.5, pady=8)
    b.bind("<Button-1>", click)
    count += 1
f.pack()
root.mainloop()