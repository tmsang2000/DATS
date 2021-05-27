# DATS

----------------------------- Dictionary Attack Test System -----------------------------

Contributor: tmsang2000
Created at: 26/05/2021
Required environment: Python 3

-------------------------------------- Description --------------------------------------

Dictionary Attack Test System is a dictionary attack demo system run directly on terminal.

The system content 6 example password file containing cryptographic values:
    - encrypted_BLAKE2B.txt
    - encrypted_MD5.txt
    - encrypted_SHA256.txt
    - encrypted_SHA512.txt
    - encrypted_SHAKE128.txt
    - encrypted_SHAKE256.txt

However, as the system was created for user to be more flexible in performing dictionary 
attack. There is also a 'password.txt' file for user to update password. Then, user can 
execute by turn the generator for generating the other cryptographic values containing 
inside each password file.

The passwordGenerator include 6 file for generating cryptographic values for 6 different 
hash method:
    - blake2bGenerator.py   - Blake2b
    - md5Generator.py       - MD5
    - sha256Generator.py    - SHA256
    - sha512Generator.py    - SHA512
    - shake128Generator.py  - Shake128
    - shake256Generator.py  - Shake256

The system content 3 dictionary file used for dictionary attack:
    - SimpleDictionary.txt (270 KB)
    - MediumDictionary.txt (14 MB)
    - LargeDictionary.txt (41 MB)

References from InsidePro:
https://web.archive.org/web/20120207113205/http://www.insidepro.com/eng/download.shtml

Finally, the 'index.py' file contain the main system for performing dictionary attack

-------------------------------------- User Guide --------------------------------------

This user guide will lead user through a short demo for the system.
(The user guide assume that the users have already install Python 3)

Step 1: Execute file 'index.py' with Python 3
Step 2: Choose the option from 1 to 6 for the password file listed
Step 3: Choose the option from 1 to 3 for the dictionary file listed
Step 4: Choose the option from 1 to 6 for the hash method listed

Finally, the result will be print out directly to the terminal

