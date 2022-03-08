#MOBILE TYPE INTERFACE
import sys
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Treeview
import mysql.connector

class AddressBook:
	def __init__(self, win):
		self.conn= mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
		self.AddressbookFrame = win
		contactsLb = Label(self.AddressbookFrame, bg="black", fg="white", text="Contacts",
								font=("Arial", 10)).place(x=5, y=25)
		self.searchInp = Entry(self.AddressbookFrame, width=40).place(x=30, y=50)
		searchIcon = PhotoImage(file="images/search.png")
		searchIconImg = searchIcon.subsample(1, 1)
		self.searchBtn = Button(self.AddressbookFrame, image=searchIconImg).place(x=275, y=50)
		self.addButton = Button(self.AddressbookFrame, text="Add Contacts", command=self.AddContactForm).place(x=310,
																												  y=47)

		self.treev = Treeview(self.AddressbookFrame, selectmode='browse')
		self.treev.place(x=45, y=100)
		self.verscrlbar = Scrollbar(self.AddressbookFrame,
									orient="vertical",
									command=self.treev.yview)
		self.verscrlbar.place(x=330, y=200)
		self.treev.configure(xscrollcommand=self.verscrlbar.set)
		self.treev["columns"] = ("Name", "Number", "Action")

		# Defining heading
		self.treev['show'] = 'headings'

		# width of columns and alignment
		self.treev.column("Name", width=100, anchor='c')
		self.treev.column("Number", width=100, anchor='c')
		self.treev.column("Action", width=100, anchor='c')

		# Headings
		# respective columns
		self.treev.heading("Name", text="Name")
		self.treev.heading("Number", text="Number")
		self.treev.heading("Action", text="Actions")
		self.fetchContact()

	def AddContactForm(self):
		self.addNew = Toplevel()
		self.addNew.configure(height=400, width=400)
		self.addNew.title= "Add new contact"

		self.firstname= StringVar()
		self.lastname= StringVar()
		self.number= StringVar()
		fnameLbl = Label(self.addNew, text="Firstname").place(x=40, y=50)
		fnameInp = Entry(self.addNew, textvariable=self.firstname, width=40).place(x=100, y=50)

		lnameLbl = Label(self.addNew, text="Lastname").place(x=40, y=100)
		lnameInp = Entry(self.addNew,textvariable=self.lastname, width=40).place(x=100, y=100)

		numberLbl = Label(self.addNew, text="Number").place(x=40, y=150)
		numInp = Entry(self.addNew, textvariable=self.number, width=40).place(x=100, y=150)

		#addButton = Button(self.addNew, text="Add", command=lambda: self.createContact(firstname, lastname, number)).place(x=200, y=200)
		addButton = Button(self.addNew, text="ADD", command=self.createContact).place(x=200, y=200)

	def createContact(self):

		firstname= (self.firstname.get())
		lastname= (self.lastname.get())
		num= (self.number.get())

		# firstname="Jeena"
		# lastname="Shrestha"
		# num="9841720695"

		#print(values)

		sql = """INSERT INTO `contact`(`firstname`, `lastname`, `number`) VALUES (%s,%s,%s);"""
		values = (firstname, lastname, num)
		print(values)
		cursor = self.conn.cursor()
		cursor.execute(sql, values)
		self.conn.commit()
		print("inserted")
		self.conn.close()

	def fetchContact(self):
		self.treev.delete(*self.treev.get_children())
		print("clicked")
		sql = """SELECT * FROM contact;"""
		cursor= self.conn.cursor()
		cursor.execute(sql)
		results=cursor.fetchall()
		for result in results:
			for dt in results:
				self.treev.insert("", 'end', text='',
						   values=(dt[1]+" "+dt[2], dt[3], 'Actions'))






root = Tk()
root.anchor("center")
root.geometry("414x650")
root.resizable(False,False)
root.configure(bg="black")

f= AddressBook(root)
root.mainloop()