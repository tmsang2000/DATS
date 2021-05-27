import hashlib

p = open('password.txt', 'r')
lines = p.read().splitlines()
p.close()

ep = open('encrypted_BLAKE2B.txt', 'w')
for line in lines:
    value = hashlib.blake2b(bytes(line, 'utf-8')).digest()
    ep.write(str(value))
    ep.write('\n')
ep.close()
