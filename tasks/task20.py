from tkinter import *
from functools import partial
def show():

   rbselection = "Gender: " + str(var.get())
   ckselection1 = str(hob1.get())
   ckselection2= str(hob2.get())
   ckselection3= str(hob3.get())
  # comment= cm1.get()
   lbShow.config(bg="pink",text = rbselection+ "\nHobbies: \n"+ ckselection1+"\n"+ckselection2+"\n"+ckselection3)



frame= Tk()
frame.geometry("700x600")
icon= PhotoImage(file="D:\pythonClass\corePython\images\icon.png")
frame.iconphoto(False, icon)
frame.resizable(False, False)
frame.title("Buttons and Boxes")
var=StringVar()
hob1=StringVar()
hob2=StringVar()
hob3=StringVar()
cmz= StringVar()
lb1=Label(frame,text="Enter text").place(x=20,y=20)
cm1= Text(frame, height=5,width=25).place(x=120, y=20)
lb2= Label (frame, text="Select Gender").place(x=20, y=150)
rb_male= Radiobutton(frame, text="male", variable=var, value="Male").place(x=120, y=150)
rb_female= Radiobutton(frame, text="female", variable=var, value="Female").place(x=120, y=170)
lb3= Label(frame, text="Hobbies").place(x=20, y=210)
ck1= Checkbutton(frame, text="Reading", variable=hob1, onvalue="Reading", offvalue=0).place(x=120, y=210)
ck2= Checkbutton(frame, text="Playing", variable=hob2, onvalue="Playing", offvalue=0).place(x=120, y=230)
ck3= Checkbutton(frame, text="Travelling", variable=hob3,  onvalue="Travelling", offvalue=0).place(x=120, y=250)
lb4= Label(frame, text="Programming").place(x=20, y=300)
lst= Listbox(frame)
lst.insert('0', "Python")
lst.insert('1', "PHP")
lst.insert('2', "Java")
lst.place(x=120, y=300)
lbShow= Label(frame)
lbShow.place(x=500,y=200)
show= partial(show)
btn= Button(frame,text="Submit", command=show).place(x=200, y=500)
frame.mainloop()
