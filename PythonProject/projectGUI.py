#MOBILE TYPE INTERFACE
import sys
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
from tkinter.ttk import Treeview
import mysql.connector

class AddressBook:
	def __init__(self, win):
		self.conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
		self.AddressbookFrame = win

		self.searchVal = StringVar()

		contactsLb = Label(self.AddressbookFrame, bg="black", fg="white", text="Contacts",
								font=("Arial", 10)).place(x=5, y=25)
		self.searchInp = Entry(self.AddressbookFrame, textvariable=self.searchVal ,width=35).place(x=30, y=50)

		#searchIcon = PhotoImage(file="images/search.png")
		#searchIconImg = searchIcon.subsample(1, 1)
		self.searchBtn = Button(self.AddressbookFrame, text="Search", command=self.search).place(x=248, y=48)


		self.addButton = Button(self.AddressbookFrame, text="Add Contacts", command=self.AddContactForm).place(x=310,
																												  y=47)

		self.editButton= Button(self.AddressbookFrame, text="Edit", command=self.loadEditContactForm).place (x=310,y=100)

		self.deleteButton = Button (self.AddressbookFrame, text="Delete", command=self.deleteContact).place(x=350,y=100)
		self.treev = Treeview(self.AddressbookFrame, selectmode='browse')
		self.treev.place(x=45, y=150)
		self.verscrlbar = Scrollbar(self.AddressbookFrame,
									orient="vertical",
									command=self.treev.yview)
		self.verscrlbar.place(x=330, y=200)
		self.treev.configure(xscrollcommand=self.verscrlbar.set)
		self.treev["columns"] = ("Firstname", "Lastname", "Number")

		# Defining heading
		self.treev['show'] = 'headings'

		# width of columns and alignment
		self.treev.column("Firstname", width=100, anchor='c')
		self.treev.column("Lastname", width=100, anchor='c')
		self.treev.column("Number", width=100, anchor='c')

		# Headings
		# respective columns
		self.treev.heading("Firstname", text="Firstname")
		self.treev.heading("Lastname", text="Lastname")
		self.treev.heading("Number", text="Number")
		self.fetchContact()

	def search(self):
		searchValue = (self.searchVal.get())
		#print(searchValue)
		self.treev.delete(*self.treev.get_children())
		sql = """
		SELECT * FROM `contact` WHERE `firstname`=%s OR `lastname`= %s OR `number`= %s
		"""
		values= (searchValue, searchValue, searchValue)
		cursor = self.conn.cursor()
		#cursor.execute(sql)
		cursor.execute(sql, values)
		results = cursor.fetchall()
		for dt in results:
			self.treev.insert("", 'end', text=dt[0],values=(dt[1], dt[2], dt[3]))
		else:
			pass



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

		sql = """INSERT INTO `contact`(`firstname`, `lastname`, `number`) VALUES (%s,%s,%s);"""
		values = (firstname, lastname, num)
		print(values)
		cursor = self.conn.cursor()
		cursor.execute(sql, values)
		self.conn.commit()
		print("inserted")
		self.fetchContact()
		self.conn.close()


	def fetchContact(self):
		self.treev.delete(*self.treev.get_children())
		sql = """SELECT * FROM contact;"""
		cursor= self.conn.cursor()
		cursor.execute(sql)
		results=cursor.fetchall()
		for dt in results:
				self.treev.insert("", 'end', text=dt[0],values=(dt[1], dt[2], dt[3]))


	def loadEditContactForm(self):

		old_firstname = self.treev.item(self.treev.selection())['values'][0]
		old_lastname = self.treev.item(self.treev.selection())['values'][1]
		old_number = self.treev.item(self.treev.selection())['values'][2]
		#print(old_firstname,old_lastname, old_number)
		self.editWin = Toplevel()
		self.editWin.configure(height=400, width=400)
		self.editWin.title = "edit contact"

		self.newfirstname = StringVar()
		self.newlastname = StringVar()
		self.newnumber = StringVar()
		self.c_id = self.treev.item(self.treev.selection())['text']
		fnameLbl = Label(self.editWin, text="Firstname").place(x=40, y=50)
		fnameInp = Entry(self.editWin, textvariable=self.newfirstname,  width=40)
		fnameInp.insert(0, old_firstname)
		fnameInp.place(x=100, y=50)

		lnameLbl = Label(self.editWin, text="Lastname").place(x=40, y=100)
		lnameInp = Entry(self.editWin, textvariable=self.newlastname,  width=40)
		lnameInp.insert(0, old_lastname)
		lnameInp.place(x=100, y=100)

		numberLbl = Label(self.editWin, text="Number").place(x=40, y=150)
		numInp = Entry(self.editWin, textvariable=self.newnumber,width=40)
		numInp.insert(0, old_number)
		numInp.place(x=100, y=150)

		updateButton = Button(self.editWin, text="Update", command=self.editContact).place(x=200, y=200)


	def editContact(self):
		id= self.c_id
		newfirstname= (self.newfirstname.get())
		newlastname= (self.newlastname.get())
		newnumber= (self.newnumber.get())

		cursor= self.conn.cursor()
		sql= """
		UPDATE `contact` SET `firstname`=%s,`lastname`= %s,`number`= %s WHERE `id`= %s 
		"""
		values = (newfirstname, newlastname, newnumber, id)
		cursor.execute(sql, values)
		self.conn.commit()
		self.fetchContact()
		self.conn.close()
		print("Updated")


	def deleteContact(self):
		c_id = self.treev.item(self.treev.selection())['text']
		res = messagebox.askquestion('', 'Are your Sure?')
		if (res == 'yes'):
			sql= "DELETE FROM contact WHERE id= %s"
			value= (c_id,)
			cursor= self.conn.cursor()
			cursor.execute(sql,value)
			self.conn.commit()
			#self.conn.close()
			print("Deleted")
			self.fetchContact()
			self.conn.close()
		else:
			pass





root = Tk()
root.anchor("center")
root.geometry("414x650")
root.resizable(False,False)
root.configure(bg="black")

f= AddressBook(root)
root.mainloop()