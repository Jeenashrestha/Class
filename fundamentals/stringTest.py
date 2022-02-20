str1 = "Jeena"
str2 = "Jeena"
str3 = '''Jeena'''
str4 = """Jeena"""
print(str1)
print(str2)
print(str3)
print(str4)
print(len(str1))
#indexing
print(str1[4]) #last index
print(str1[-1]) #last index


#slicing
print(str1[0:]) #0 to last
print(str1[:]) #0 to last
print(str1[:4]) #0 to third
print(str1[1:4]) #1 to third
print()
print(str1[0:5:2]) #start: stop: step JEENA
print(str1[::2]) #skip by 2
print(str1[::1]) #skip by 1
print(str1[::9]) #(has no index error)

import sys
print(id(str1))
print(len(str1))
print(min(str1))
print(max(str1))
print(sys.getsizeof(str1))
print(sys.getsizeof(str1[2]))