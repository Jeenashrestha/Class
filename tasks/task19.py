from tkinter import *
from functools import partial
def onClick(lbDisplay, num1, num2):
    n1 = (num1.get())
    n2 = (num2.get())

    if n1!='' and n2!='':
        lbDisplay.config(background="pink",padx=20, pady=10,text= "Sum: "+str(int(n1)+int(n2)), font=10)
    else:
        lbDisplay.config(background="red", padx=20, pady=10, text="Please enter both numbers", font=10)
    return


frame= Tk()
num1= StringVar()
num2= StringVar()
frame.geometry("400x300")
frame.resizable(False,False)
icon= PhotoImage(file="D:\pythonClass\corePython\images\icon.png")
frame.iconphoto(False, icon)
frame.title("Calculator")
lb1= Label (frame,text="Enter num1: ", bg="grey", padx=5, pady=5).place(x=20,y=20)
inp1 =Entry(frame, textvariable=num1, width=40).place(x=110,y=25)
lb2= Label (frame,text="Enter num2: ", bg="grey", padx=5, pady=5).place(x=20,y=50)
inp2 =Entry(frame, textvariable=num2, width=40).place(x=110,y=55)
lbDisplay=Label(frame)
lbDisplay.place(x=130, y=200)
onClick= partial(onClick, lbDisplay,num1,num2)
subID= Button(frame, text="Submit", command=onClick).place(x=150, y=120)
frame.mainloop()