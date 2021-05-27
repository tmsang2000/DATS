import hashlib

p = open('password.txt', 'r')
lines = p.read().splitlines()
p.close()

ep = open('encrypted_SHAKE256.txt', 'w')
for line in lines:
    value = hashlib.shake_256(bytes(line, 'utf-8')).digest(15)
    ep.write(str(value))
    ep.write('\n')
ep.close()
