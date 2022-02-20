import sys

import mysql
from mysql.connector import *

def connectDB(databaseName,password):
    result=False
    try:
        conn=mysql.connector.connect(host='localhost',database=databaseName, user='root', password=password)
        result=True
        if conn.is_connected():
            cursor = conn.cursor()
            query = "Select database();"
            cursor.execute(query)
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except:
            print("Connection failed: ", sys.exc_info()[1])

    finally:
            return result

#print(connectDB('broadway' , ''))

def createTable():
    result=False
    try:
        conn = mysql.connector.connect(host="localhost", database= "broadway", user="root", password="")
        if conn.is_connected:
            createSql = """
            CREATE TABLE students (
            id int,
            name  varchar(255),
            class varchar(255),
            sub1 int,
            sub2 int,
            sub3 int
            );
            """
        cursor = conn.cursor()
        cursor.execute(createSql)
        print("Table Created")

    except Error as e:
        print("Error: " ,e)

    finally:
        return result



def addRecord(record):
    result = False
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        #if conn.is_connected:
        insertSql = """
                        INSERT INTO students(name, class, sub1, sub2, sub3) VALUES (%s,%s,%s,%s,%s);
                        """
        cursor = conn.cursor()
        added= cursor.execute(insertSql, record)
        conn.commit()
        if added:
            print("Record successfully added.")


    except Error as e:
        print("Error: ", e)

    finally:
        return result

def displayAllRecords():
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        if conn.is_connected:
            displaySql = """SELECT * FROM students;"""
            cursor = conn.cursor()
            cursor.execute(displaySql)
            results = cursor.fetchone()
            print("********** STUDENT RECORDS ********** ")

            print(results)
            id=results[0]
            name= results[1]
            grade= results[2]
            sub1= int(results[3])
            sub2= int(results[4])
            sub3= int(results[5])
            total= sub1+sub2+sub3
            print ("ID: ", id)
            print("Name: ",name,"\nGrade: ",grade,"\nMarks Obtained: ","\nSub1: ",sub1,"\nSub2: ",sub2,"\nSub3: ",sub3)
            print ("Total: ", total)
            print("Average: ", total/3)
            if sub1>=40 and sub2>=40 and sub3>=40 :
                print ("Result: Pass")
            else:
                print("Result: Fail")
            print()

            conn.close()
    except Error as e:
        print("Error: ", e)
    finally:
        pass

def searchID(id):
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        if conn.is_connected:
            fetchSql = """SELECT * FROM students WHERE id= %s;"""
            cursor = conn.cursor()
            cursor.execute(fetchSql,id)
            results = cursor.fetchone()
            print(results)
            conn.close()
    except Error as e:
        print("Error: ", e)
    finally:
        pass

def updateRecord(record):
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        if conn.is_connected:
            cursor = conn.cursor()
            updateSql = """
            UPDATE students SET name=%s WHERE id=%s;
            """
            cursor.execute(updateSql,record)
            conn.commit()
            print("Updated record successfully.")
            conn.close()
    except Error as e:
        print("Error: ", e)
    finally:
        pass

def deleteId(id):
    try:
        conn = mysql.connector.connect(host="localhost", database="broadway", user="root", password="")
        if conn.is_connected:
            deleteSql = """DELETE  FROM students WHERE id= %s;"""
            cursor = conn.cursor()
            query = cursor.execute(deleteSql,id)
            conn.commit()
            conn.close()
            if query:
             print("Record deleted Successfully.")
    except Error as e:
        print("Error: ", e)
    finally:
        pass


text= "MAIN MENU\n1. Add new record\n2. Display all record(s)\n3. Search record based on id\n4. Search and edit\n5. Search and delete\n6. Exit "
print(text)
userInp = input("Enter your choice: ")
if userInp=="1":
    name= input("Enter name: ")
    stclass= int(input("Enter class: "))
    stclass = input("Enter class: ")
    sub1 = input("Enter sub1: ")
    sub2 = input("Enter sub2: ")
    sub3 = input("Enter sub3: ")
    record= [name, stclass, sub1, sub2, sub3]
    addRecord(record)
elif userInp=="2":
    displayAllRecords()
elif userInp=="3":
    id= list(input("Enter the id you want to search: "))
    searchID(id)
elif userInp=="4":
    id=int(input("Enter the id you want to update: "))
    name= input ("Enter new name: ")
    record=(name, id)
    #print(record)
    updateRecord(record)
elif userInp=="5":
    id = list(input("Enter the id you want to delete: "))
    deleteId(id)
else:
    del userInp
    print("Invalid Choice")