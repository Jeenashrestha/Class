#get values in a memory address
import ctypes
a = True
b = False
address = id(a)
print(ctypes.cast(address, ctypes.py_object).value)