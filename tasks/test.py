import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="broadway"
)

####### end of connection ####
displaySql = """SELECT * FROM infosys;"""
cursor = conn.cursor()
cursor.execute(displaySql)
i=0
for student in cursor:
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
my_w.mainloop()