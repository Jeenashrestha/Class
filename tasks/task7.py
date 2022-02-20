#display all user defined variables python

builtIns = set(dir())

a = "Jeena"
b = 1

userDefined = set(dir()) - builtIns
for name in userDefined:
    # Exclude the un-necessary variable named not_my_data
    if name != "builtIns":
        val = eval(name)
        print(name)
