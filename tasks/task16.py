from tkinter import *
from functools import partial
def onClick(lbDisplay, yourId):
    id1 = (yourId.get())
    if id1!='':
        lbDisplay.config(background="pink",padx=20, pady=10,text= "Your ID is "+ id1, font=10)
    else:
        lbDisplay.config(background="red", padx=20, pady=10, text="Please Enter your ID", font=10)
    return


frame= Tk()
yourId= StringVar()
frame.geometry("400x300")
frame.resizable(False,False)
frame.title("Information System")
lbID= Label (frame,text="Enter your ID: ", bg="grey", padx=5, pady=5).place(x=20,y=20)
inpID =Entry(frame, textvariable=yourId, width=40).place(x=110,y=25)
lbDisplay=Label(frame)
lbDisplay.place(x=130, y=150)
onClick= partial(onClick, lbDisplay,yourId)
subID= Button(frame, text="Submit", command=onClick).place(x=200, y=60)
frame.mainloop()