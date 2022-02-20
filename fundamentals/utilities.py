from pkg1 import packagetest
import os
from os import listdir
from os.path import isfile, join
print(packagetest.var1)
print(packagetest.f1())

obj1= packagetest.Test()
obj1.f2()

print(help(os))

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]