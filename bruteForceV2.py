# Name : bruteForceV2.py
# Author : Joe Gumke
# Date : 9-12-18
# Description : generates wordlist and brute forces the hash list
# Example : python bruteForce.py #LENGTH_OF_WORD HASH_LIST Algorithm_Type
# Usage Run : python .\bruteForceV2.py 5 .\hashes\eharmony\eharmonypasswords.txt md5

# Enter libraries
import string
import sys
from itertools import product
import hashlib

# Enter arguments for length of string
stringLength = sys.argv[1]
stringLength = int(stringLength)

hashType = (getattr(hashlib,str(sys.argv[3])))

# Enter arguments for hashlist
hashList = []

# put hashed passwords into a list
with open(sys.argv[2]) as hashFile:
    for i in hashFile:
    # remove cracked rainbow table hits
        if not i.startswith('00000'):
            temp = i.strip('\n')
            temp1 = temp.strip()
            hashList.append(temp1)

counter = 0
wordCounter = 0
for i in range(len(str(stringLength))):
    for i in product(string.printable, repeat=stringLength):
        result = ''.join(i)
        resultString=str(result)
        result = resultString.encode('utf-8').rstrip()
        hashResult = hashType(result)
        hashed = hashResult.hexdigest()
        wordCounter += 1
        if hashed in hashList:
            counter += 1
            print("*** MATCH - HASH : %s Name : %s" % (hashed, resultString))
print("Number of matches :", counter)
print("Number of Words Attempted :", wordCounter)
