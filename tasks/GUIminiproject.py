import sys
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import mysql.connector

def insertDb():
    try:
        mydb= mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        name = (userName.get())
        address = (userAddress.get())
        gender = (userGender.get())
        hobbies = (userHobbies1.get()) + " " + (userHobbies2.get()) + " " + (userHobbies3.get())
        academics= (userAcad.get())
        for i in listAge.curselection():
            age = (listAge.get(i))
        sql = """INSERT INTO `infosys`(`name`, `address`, `gender`, `hobbies`, `academics`, `age`) VALUES (%s,%s,%s,%s,%s,%s);"""
        values=(name,address, gender, hobbies, academics, age)
        cursor= mydb.cursor()
        cursor.execute(sql, values)
        mydb.commit()
        print("*****inserting into database*****")
        print("inserted")
        mydb.close()

    except:
     print("error: ", sys.exc_info()[0])
    finally:
        pass

def loadTable():
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        displaySql = """SELECT * FROM infosys;"""
        cursor = conn.cursor()
        cursor.execute(displaySql)
        i = 0
        for student in cursor:
            for j in range(len(student)):
                infosysTable = Entry(infosys, width=10, fg='blue')
                infosysTable.grid(row=i, column=j)
                infosysTable.insert(END, student[j])
            i = i + 1
        conn.close()
    except:
        print("error: ", sys.exc_info()[0])

    finally:
        pass

def deleteAllDb():
    try:
        mydb = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        delSql = """ DELETE FROM infosys """
        res=messagebox.askquestion('', 'Are your Sure?')
        if(res=='yes'):
            cursor = mydb.cursor()
            cursor.execute(delSql)
            mydb.commit()
            mydb.close()
            print("Deleted all records")

        else:
            mydb.close()

    except:
        print("Error: ", sys.exc_info()[0])
    finally:
        pass

def searchInfo():
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        if conn.is_connected:
            fetchSql = """SELECT * FROM infosys WHERE name= %s;"""
            name= (userSearch.get())
            value = (name,)
            cursor = conn.cursor()
            cursor.execute(fetchSql, value)
            results = cursor.fetchall()
            trv =Treeview(infosys, selectmode='browse')
            trv.grid(row=1, column=1, padx=20, pady=20)
            # number of columns
            trv["columns"] = ("1", "2", "3", "4", "5")

            # Defining heading
            trv['show'] = 'headings'

            # width of columns and alignment
            trv.column("1", width=30, anchor='c')
            trv.column("2", width=80, anchor='c')
            trv.column("3", width=80, anchor='c')
            trv.column("4", width=80, anchor='c')
            trv.column("5", width=80, anchor='c')

            # Headings
            # respective columns
            trv.heading("1", text="id")
            trv.heading("2", text="Name")
            trv.heading("3", text="Class")
            trv.heading("4", text="Mark")
            trv.heading("5", text="Gender")

            for r in results:
                for dt in results:
                    trv.insert("", 'end', iid=dt[0], text=dt[0],
                               values=(dt[0], dt[1], dt[2], dt[3], dt[4]))
            conn.close()
    except:
        print("Error: ")
    finally:
        pass


infosys= Tk()
userName= StringVar()
userAddress= StringVar()
userGender= StringVar()
userHobbies1= StringVar()
userHobbies2= StringVar()
userHobbies3= StringVar()
userAge = StringVar()
userAcad = StringVar()
userSearch= StringVar()

infosys.geometry("600x800")
infosys.resizable(False, False)
#name
nameLabel = Label(infosys, text="Name: ").place(x=20,y=40)
nameInp = Entry(infosys, textvariable=userName, width=40).place(x=80, y=42)

#address
addressLabel = Label(infosys, text= "Address: "). place(x=20, y=80)
addressInp = Entry(infosys, textvariable=userAddress, width=40).place(x=80, y=82)

#gender
genderLabel = Label (infosys, text="Gender: ").place(x=20, y= 120)
rbFemale = Radiobutton(infosys, text="Female", value="Female", variable=userGender).place(x=80, y=120)
rbMale = Radiobutton(infosys, text="Male", value="Male", variable=userGender).place(x=150, y=120)
rbOthers = Radiobutton(infosys, text="Others", value="Others", variable=userGender).place(x=220, y=120)

#hobbies
labelHobbies = Label(infosys, text="Hobbies: ").place(x=20, y= 160)
ckHobbies1 = Checkbutton(infosys, text="Swimming", variable=userHobbies1, onvalue="Swimming", offvalue=0).place(x=80, y=160)
ckHobbies2 = Checkbutton(infosys, text="Football", variable=userHobbies2, onvalue="Football", offvalue=0).place(x=200, y=160)
ckHobbies3 = Checkbutton(infosys, text="Basketball",variable=userHobbies3,  onvalue="Basketball", offvalue=0).place(x=320, y=160)

#Age group
labelAge= Label(infosys, text="Age: ").place(x=20, y= 200)
listAge= Listbox(infosys, width=40, height=10)
listAge.insert('0',"1-17")
listAge.insert('1',"18-21")
listAge.insert('2',"21-30")
listAge.insert('3',"30-40")
listAge.insert('4',"40-50")
listAge. place(x=80, y=200)

#academics
labelAcad= Label(infosys, text="Academics: ").place(x=20, y=400)

# Combobox creation

acadchosen = Combobox(infosys, width = 27, textvariable = userAcad)
acadchosen['values'] = ('+2',
						'Bachelors',
						'Masters')
acadchosen.place(x=80, y=400)
acadchosen.current(1)

#save button
btnSave= Button(infosys, text="Save", command=insertDb).place(x=150, y=500)

#delete button
btnDelete =Button(infosys, text="Delete All", command=deleteAllDb).place(x=210,y=500)

#search
inpSearch= Entry(infosys, width=20, textvariable=userSearch).place(x=300, y=505)
btnSearch= Button(infosys, text="Search", command=searchInfo).place(x=425, y=500)

loadTable()
infosys.mainloop()