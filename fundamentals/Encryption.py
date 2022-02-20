from cryptography.fernet import Fernet

#GENETARE KEY
# key = Fernet.generate_key()
# f = open('key.txt', "wb")
# f.write(key)
# f.close()

#SAVE KEY IN FILE OR DATABASE
f = open('key.txt', "rb")
key1=f.read()
#print(key1)
f.close()
#print(key1.decode("utf-8"))

#ENCRYPT DATA
str1 ="Broadway Infosys"
str2 = str1.encode()
fernt= Fernet(key1)
str3 = fernt.encrypt(str2)
print(str3)

#DECRYPT DATA
fernt=Fernet(key1)
str4= fernt.decrypt(str3)
str4 = str4.decode("utf-8")
print(str4)

