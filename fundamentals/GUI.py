from tkinter import *
"""
frame= Tk()
frame.mainloop()
"""
"""frame= Tk()
frame.geometry("400x500")
frame.mainloop()"""

frame= Tk()
frame.geometry("400x600")
#icon= PhotoImage(file="D:\pythonClass\corePython\images\icon.png")
#frame.iconphoto(False, icon)
frame.resizable(False, False)
frame.title("Calculator")
lb1=Label(frame,text="Enter comment").place(x=20,y=20)
cm1= Text(frame, height=5,width=25).place(x=120, y=20)
lb2= Label (frame, text="Select Gender").place(x=20, y=150)
rb_male= Radiobutton(frame, text="male").place(x=120, y=150)
rb_female= Radiobutton(frame, text="female").place(x=120, y=170)
lb3= Label(frame, text="Hobbies").place(x=20, y=210)
ck1= Checkbutton(frame, text="Reading").place(x=120, y=210)
ck2= Checkbutton(frame, text="Playing").place(x=120, y=230)
ck3= Checkbutton(frame, text="Travelling").place(x=120, y=250)
lb4= Label(frame, text="Programming").place(x=20, y=300)
lst= Listbox(frame)
lst.insert('0', "Python")
lst.insert('1', "PHP")
lst.insert('2', "Java")
lst.place(x=120, y=300)
btn= Button(frame,text="Submit").place(x=200, y=500)
frame.mainloop()
