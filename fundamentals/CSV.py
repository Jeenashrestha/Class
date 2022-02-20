import csv
import sys

"""
#WRITE ON CSV
filename = "D:/file/data.csv"
headingRow = ['SN', 'Name', 'Address']
r1 = ['1', 'Jeena', 'Imadol']
try:
    csvFile= open(filename, "w")
    writer= csv.writer(csvFile)
    writer.writerow(headingRow)
    writer.writerow(r1)
except:
    print("Error: ", sys.exc_info())

finally:
    del filename
"""
#READ ON CSV
filename = "D:/file/data.csv"
try:
    csvFile= open(filename, mode="r")
    reader= csv.reader(csvFile)
    for row in reader:
        if len(row)>0:
            print(','.join(row))
except:
    print("Error: ", sys.exc_info())

finally:
    del filename

