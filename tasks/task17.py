#Encrypt and decrypt content of a whole file
from cryptography.fernet import Fernet

# key= Fernet.generate_key()
# f = open("key1.txt","wb")
# f.write(key)
# f.close()

f= open ("key1.txt","rb")
key= f.read()
f.close()

def encrypt():
    originalFile = open("file.txt","r")
    originalData= originalFile.read();
    originalFile.close()

    frnt= Fernet(key)
    encodedData = originalData.encode()
    encryptedData= frnt.encrypt(encodedData)
    #print(encryptedData)

    orignalFile1= open("file.txt", "wb")
    orignalFile1.write(encryptedData)
    orignalFile1.close()
    print("Data Encrypted")

def decrypt():
    encrytedFile= open("file.txt", "rb")
    encryptedData= encrytedFile.read()
    encrytedFile.close()
    frnt= Fernet(key)
    decryptedData= frnt.decrypt(encryptedData)
    decodedData= decryptedData.decode("utf-8")
    #print(decodedData)

    decryptedFile= open("file.txt", "w")
    decryptedFile.write(decodedData)
    decryptedFile.close()
    print("Data Decrypted")

def readFile():
    f = open("file.txt", "r")
    print(f.read())
    f.close()

#encrypt()
decrypt()
readFile()
