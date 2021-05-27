import hashlib

print('Password File:\n1. encrypted_SHA256.txt\n2. encrypted_MD5.txt\n3. encrypted_SHA512.txt\n4. encrypted_BLAKE2B.txt\n5. encrypted_SHAKE128.txt\n6. encrypted_SHAKE256.txt')
print("Choose file (1-6): ")
option = input()
encryptedFile = ''
while int(option) < 1 or int(option) > 6:
    print("Wrong option! Please choose again: ")
    option = input()
if option == '1':
    encryptedFile = 'encrypted_SHA256.txt'
elif option == '2':
    encryptedFile = 'encrypted_MD5.txt'
elif option == '3':
    encryptedFile = 'encrypted_SHA512.txt'
elif option == '4':
    encryptedFile = 'encrypted_BLAKE2B.txt'
elif option == '5':
    encryptedFile = 'encrypted_SHAKE128.txt'
elif option == '6':
    encryptedFile = 'encrypted_SHAKE256.txt'

ep = open(encryptedFile, 'r')
lines = ep.read().splitlines()
ep.close()

print('Dictionary file:\n1. SimpleDictionary.txt\n2. MediumDictionary.txt\n3. LargeDictionary')
print("Choose file (1-3): ")
option = input()

while int(option) < 1 or int(option) > 3:
    print("Wrong option! Please choose again: ")
    option = input()

dicFile = ''
if option == '1':
    dicFile = 'SimpleDictionary.txt'
elif option == '2':
    dicFile = 'MediumDictionary.txt'
elif option == '3':
    dicFile = 'LargeDictionary.txt'
d = open(dicFile, 'r')
dic = d.read().splitlines()

print('Hash method:\n1. SHA256\n2. MD5\n3. SHA512\n4. BLAKE2B\n5. SHAKE128\n6. SHAKE256')
print("Choose method (1-6): ")
option = input()

while int(option) < 1 or int(option) > 6:
    print("Wrong option! Please choose again: ")
    option = input()

result = []
value = ''
for i in dic:
    if option == '1':
        value = str(hashlib.sha256(bytes(i, 'utf-8')).digest())
    elif option == '2':
        value = str(hashlib.md5(bytes(i, 'utf-8')).digest())
    elif option == '3':
        value = str(hashlib.sha512(bytes(i, 'utf-8')).digest())
    elif option == '4':
        value = str(hashlib.blake2b(bytes(i, 'utf-8')).digest())
    elif option == '5':
        value = str(hashlib.shake_128(bytes(i, 'utf-8')).digest(15))
    elif option == '6':
        value = str(hashlib.shake_256(bytes(i, 'utf-8')).digest(15))
    for j in lines:
        if value == j:
            result.append(i)

print("Matched: ", len(result))
print("Result: ", result)

d.close()