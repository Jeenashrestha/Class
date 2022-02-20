from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
root.geometry("400x600")
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel).place(x=20, y=20)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel).place(x=20, y=50)
R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel).place(x=20, y=70)

label = Label(root)
label.place(x= 20, y=90)
root.mainloop()