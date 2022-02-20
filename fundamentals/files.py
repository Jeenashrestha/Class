import os.path
import sys

"""path="D:/file/"
filename= "myfile.txt"
completeName =path+filename
content= "This  file is new"
try:
    f= open(completeName,"w")
    f.write(content)
    f.close()
    print("File successfully created")
except:
    print("error: ", sys.exc_info()[1])
finally:
    del filename
    del content
    del path

path="D:/file/"
filename= "myfile.txt"
completeName =path+filename
try:

    g= open(completeName,"r")
    print(g.read())
    g.close()
except:
    print("error: ", sys.exc_info())
finally:
    del filename
    del path
"""
path = "D:/file/"
filename = "myfile.txt"
completeName = path + filename
contentAppend= "Appended content"
try:
    h = open(completeName, "a")
    h.write(contentAppend)
    h.close

    print ("*******After appending*******")

    i = open("D:/file/myfile.txt", "r")
    print(i.read())
    i.close()
except:
    print("error: ", sys.exc_info())
finally:
    del filename
    del path

