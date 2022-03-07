#MOBILE TYPE INTERFACE
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Treeview


def loadCurrencyConverter():
	currencyConvFrame= Frame(homesc, bg="black", width=470, height=650).place(x=0,y=0)

	fromInp= Entry(currencyConvFrame, width=20). place(x=100, y=250)

	fromOptions = ["$","NPR", "INR"]
	fromDefaultOpt= StringVar(currencyConvFrame)
	fromDefaultOpt.set(fromOptions[0])
	fromDrp= OptionMenu(currencyConvFrame, fromDefaultOpt,*fromOptions).place(x=230,y=240)

	toInp = Entry(currencyConvFrame, width=20).place(x=100, y=340)

	toOptions = ["$", "NPR", "INR"]
	toDefaultOpt = StringVar(currencyConvFrame)
	toDefaultOpt.set(fromOptions[0])
	toDrp = OptionMenu(currencyConvFrame, toDefaultOpt, *toOptions).place(x=230, y=330)

	convertBtn= Button(currencyConvFrame, text="CONVERT").place(x=170, y=430)




def loadAddressBook():
# #Addressbook frame


	AddressbookFrame= Frame(homesc, bg="black", width=470, height=650).place(x=0,y=0)

	BtnBack = Button(AddressbookFrame, text="←", width=5).place(x=5, y=5)
	contactsLb= Label(AddressbookFrame,bg="black", fg="white", text= "Contacts", font=("Arial", 10)).place(x=5,y=25)

	searchInp = Entry(AddressbookFrame, width=50).place(x=45, y=50)
	searchIcon= PhotoImage(file="images/search.png")
	searchIconImg= searchIcon.subsample(1,1)
	searchBtn= Button(AddressbookFrame,image=searchIconImg).place(x=350,y=50)

	# Using treeview widget
	treev = Treeview(AddressbookFrame, selectmode ='browse')
	treev.place(x=45,y=100)

	verscrlbar = Scrollbar(AddressbookFrame,
							orient ="vertical",
							command = treev.yview)
	verscrlbar.place(x=330,y=200)

	treev.configure(xscrollcommand = verscrlbar.set)

	treev['columns']=('Name')
	treev.column('#0', width=0, stretch=NO)

	treev.column('Name', anchor=CENTER, width=300)


	treev.heading('Name', text='', anchor=CENTER)

	treev.insert(parent='', index=0, iid=0, text='', values=('Vineet'))
	treev.insert(parent='', index=1, iid=1, text='', values=('Anil'))
	treev.insert(parent='', index=2, iid=2, text='', values=('Vinod'))
	treev.insert(parent='', index=3, iid=3, text='', values=('Vimal'))
	treev.insert(parent='', index=4, iid=4, text='', values=('Manjeet'))
	treev.insert(parent='', index=5, iid=5, text='', values=('Vineet'))
	treev.insert(parent='', index=6, iid=6, text='', values=('Anil'))
	treev.insert(parent='', index=7, iid=7, text='', values=('Vinod'))
	treev.insert(parent='', index=8, iid=8, text='', values=('Vimal'))
	treev.insert(parent='', index=9, iid=9, text='', values=('Manjeet'))
	treev.insert(parent='', index=10, iid=10, text='', values=('Manjeet'))
	treev.insert(parent='', index=11, iid=11, text='', values=('Vineet'))
	treev.insert(parent='', index=12, iid=12, text='', values=('Anil'))
	treev.insert(parent='', index=13, iid=13, text='', values=('Vinod'))
	treev.insert(parent='', index=14, iid=14, text='', values=('Vimal'))
	treev.insert(parent='', index=15, iid=15, text='', values=('Manjeet'))


def loadCalculator():


#CALCULATOR
	calcOutFrame= Frame(homesc, bg="white", width=470, height=650).place(x=0,y=0)

	# def clear_frame():
	# 	for widgets in calcOutFrame.winfo_children():
	# 		widgets.destroy()

	calcFrame= Frame(calcOutFrame,).place(x=0,y=200)

	NumberLbl= Label(calcFrame, bg="white", text="12+10= 22").grid(row=0, column=1, columnspan=4)

	BtnClr = Button(calcFrame, text= " AC " , bg="black", height=5, width=10, fg="white").grid(row=1, column=1)
	BtnPM= Button(calcFrame, text= " +/- " , bg="black", height=5, width=10, fg="white").grid(row=1, column=2)
	BtnPercent = Button(calcFrame, text= " 1 " , bg="black", height=5, width=10, fg="white").grid(row=1, column=3)
	BtnDiv = Button(calcFrame, text= " ÷ " , bg="orange", height=5 ,width=10, fg="white").grid(row=1, column=4)

	Btn1 = Button(calcFrame, text= " 1 " , bg="black", height=5, width=10, fg="white").grid(row=2, column=1)
	Btn2 = Button(calcFrame, text= " 2 " , bg="black", height=5, width=10, fg="white").grid(row=2, column=2)
	Btn3 = Button(calcFrame, text= " 3 " , bg="black", height=5, width=10, fg="white").grid(row=2, column=3)
	BtnMul= Button(calcFrame, text= " × " , bg="orange", height=5 ,width=10, fg="white").grid(row=2, column=4)

	Btn5 = Button(calcFrame, text= " 5 " , bg="black", height=5 ,width=10, fg="white").grid(row=3, column=2)
	Btn4 = Button(calcFrame, text= " 4 " , bg="black", height=5 ,width=10, fg="white").grid(row=3, column=1)
	Btn6 = Button(calcFrame, text= " 6 " , bg="black", height=5 , width=10, fg="white").grid(row=3, column=3)
	BtnSum = Button(calcFrame, text= " + " , bg="orange", height=5, width=10, fg="white").grid(row=3, column=4)

	Btn7 = Button(calcFrame, text= " 7 " , bg="black", height=5 ,width=10, fg="white").grid(row=4, column=1)
	Btn8 = Button(calcFrame, text= " 8 " , bg="black", height=5 ,width=10, fg="white").grid(row=4, column=2)
	Btn9 = Button(calcFrame, text= " 9 " , bg="black", height=5 ,width=10, fg="white").grid(row=4, column=3)
	BtnSub = Button(calcFrame, text= " - " , bg="orange", height=5 ,width=10, fg="white").grid(row=4, column=4)

	Btn0 = Button(calcFrame, text= " 0 " , bg="black", height=5, fg="white", width=21).grid(row=5, column=1 , columnspan=2)
	BtnPoint = Button(calcFrame, text= " . " , bg="black", height=5, width=10, fg="white").grid(row=5, column=3)
	BtnEquals = Button(calcFrame, text= " = " , bg="orange", height=5, width=10, fg="white").grid(row=5, column=4)




homesc = Tk()
homesc.anchor("center")
homesc.geometry("414x650")
homesc.resizable(False,False)
homesc.configure(bg="#3380a1")

contactBookImg = PhotoImage(file="images/contacts.png")
contactBookBtn = Button(homesc, image=contactBookImg, command=loadAddressBook).place(x=80, y=300)

calculatorImg= PhotoImage(file="images/calculator.png")
calculatorBtn = Button(homesc, image=calculatorImg, command=loadCalculator).place(x=180, y=300)

currencyImg = PhotoImage(file="images/currency.png")
currencyConverterImg = currencyImg.subsample(1, 1)
currencyConverterBtn = Button(homesc, image=currencyConverterImg, command=loadCurrencyConverter).place(x=280, y=300)




homesc.mainloop()