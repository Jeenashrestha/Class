# Python program to print a given number in words

def toWords(num):
	lenOfNum= len(num)
	if lenOfNum==0:
		print("Empty number")
	if (lenOfNum>4):
		print ("Not supported")

	ones= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	tens= ["","ten", "eleven", "twelve", "thirteen","fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
	tens_pow= ["hundred", "thousand"]
	tens_mul= ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	if lenOfNum==1:
		print (ones[int(num)])
	if lenOfNum==2:
		if int(num) < 20:
			print (tens[int(num)-9])
		else:
			l1= [int(d) for d in num]
			if l1[0]>0:
				a=l1[0]
				print(tens_mul[a], end=" ")
			if l1[1]>0:
				b=l1[1]
				print (ones[b])

	if lenOfNum==3:
		l1= [int(d) for d in num]
		if l1[0]>0:
			a = l1[0]
			print (ones[a], tens_pow[0] , end=" ")
		if l1[1] > 0:
			a = l1[1]
			print(tens_mul[a], end=" ")
		if l1[2] > 0:
			b = l1[2]
			print(ones[b])

	if lenOfNum==4:
		l1= [int(d) for d in num]
		if l1[0]<=9:
			i=l1[0]
			print(ones[i], tens_pow[1], end=" ")
		if l1[1]>0:
			a = l1[1]
			print (ones[a], tens_pow[0] , end=" ")
		if l1[2] > 0:
			a = l1[2]
			print(tens_mul[a], end=" ")
		if l1[3] > 0:
			b = l1[3]
			print(ones[b])

num = input("Enter a number: ")
toWords(num)