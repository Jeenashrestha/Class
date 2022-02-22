import sys
from tkinter import *
from tkinter.ttk import Combobox
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
    except:
        print("error: ", sys.exc_info()[0])

    finally:
        pass


infosys= Tk();
userName= StringVar()
userAddress= StringVar()
userGender= StringVar()
userHobbies1= StringVar()
userHobbies2= StringVar()
userHobbies3= StringVar()
userAge = StringVar()
userAcad = StringVar()

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
btnSave= Button(infosys, text="Save", command=insertDb).place(x=250, y=500)
loadTable()
infosys.mainloop()