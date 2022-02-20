#Loop statements

#1. While loop
'''
startNum =1
endNum=10
while(startNum<=endNum):
    print(startNum, " Hi")
    startNum+=1

print()

#2. for loop
for i in range(0, 5):
	print(i)
'''

'''
#3. list iteration
list1= [1,2,3,4,5,6]
for item in list1:
       if item==3:
           print(item, "is found")
        else:
            print ("not found")
'''
#4. Nested for loop
for i in range(1,5):
    for j in range(i):
        print (i, end=" ")
    print()

#5. print items in from last to first using for in loop
list1= [1,2,3,4,5,6,7]
for items in reversed(list1):
    print( items, end =" ")

print()

list1= ['a' , 'b' , 'c' , 'd' , 'e']
for items in range( len(list1)-1 , -1, -1) :
    print(list1[items], end=" ")

print()

list1= ['a' , 'b' , 'c' , 'd' , 'e']
i=len(list1)-1
while(i>=0):
    print(list1[i], end=" ")
    i=i-1
