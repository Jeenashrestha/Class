#CRUD operations
import sqlite3
import sys

#CREATE DATABASE
def connectdb(db_name):
    result = False
    try:
        conn = sqlite3.connect(db_name)
        conn.close()
        result=True
    except:
        print("Error: " , sys.exc_info()[1])
    finally:
        return result



#CREATE DATABASE TABLE
def createTable():
    result = False
    sql = """

    CREATE TABLE IF NOT EXISTS users(
    pid integer ,
    fullname text,
    address text
 )
"""
    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       cursor.execute(sql)
       conn.commit()
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result

#INSERT INTO DATABASE TABLE

def insertRecord(record):
    result = False
    sql = """
    INSERT INTO users(pid, fullname, address) VALUES (?, ? , ?)
"""
    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       cursor.execute(sql, record)
       conn.commit()
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result

def readAll():
    result = False
    sql = """
    SELECT * FROM users
"""
    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       records = cursor.execute(sql)
       for record in records:
        print(record)
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result


def searchRecord(pid):
    result = False
    sql = " SELECT * FROM users WHERE pid= ?"
    values=(pid,)
    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       records = cursor.execute(sql, values)
       for record in records:
        print(record)
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result

def deleteRecord(pid):
    result = False
    sql = " DELETE FROM users WHERE pid= ?"
    values=(pid,)
    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       cursor.execute(sql, values)
       conn.commit()
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result


def updateRecord(record):
    result = False
    sql = " UPDATE users SET  fullname=? , address=? WHERE pid=? "

    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       cursor.execute(sql, record)
       conn.commit()
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result

def partialUpdate(record):
    result = False
    sql = " UPDATE users SET  fullname=?  WHERE pid=? "

    try:
       conn = sqlite3.connect("StudentRecord.db")
       cursor = conn.cursor()
       cursor.execute(sql, record)
       conn.commit()
       conn.close()
       result = True
    except:
       print("Error: ", sys.exc_info()[1])
    finally:
       return result

#print(connectdb("StudentRecord.db"))
#print(createTable())
#print(insertRecord([2, 'Apple', 'Tree']))
#print(searchRecord(1))
#print(readAll())
#print(deleteRecord(2))
#print(updateRecord(['Apples', 'Trees', '1']))
#print(partialUpdate(['Jeena', '1']))
print(readAll())


#Exploring Database (GO TO sqliteonline.com AND OPEN DATABASE FILE)

