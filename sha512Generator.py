import hashlib

p = open('password.txt', 'r')
lines = p.read().splitlines()
p.close()

ep = open('encrypted_SHA512.txt', 'w')
for line in lines:
    value = hashlib.sha512(bytes(line, 'utf-8')).digest()
    ep.write(str(value))
    ep.write('\n')
ep.close()
