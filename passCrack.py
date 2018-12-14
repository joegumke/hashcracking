# Name: passcrack.py
# Author: Joe Gumke
# Description: Iterates through, hashes them, and writes them out to a dictionary.
# Usage : Enter 3 arguments. 1st = word list. 2 =  hash list. 3 = hash Algorithm
# Then can be compared to against a list of known hashes.
# Example : python .\passCrack.py .\wordlists\10-million-password-list-top-1000000.txt .\hashes\eharmony\eharmonypasswords.txt md5

# Import Libraries
import sys
import hashlib

# Build Empty Dictionary
dictionary = {}
hashList =[]
# Welcome Statement
print("*** Welcome to:", sys.argv[0])
print("*** Number of arguments: ", len(sys.argv))
print("*** The arguments are:", str(sys.argv))
print("*** WordList processing:", sys.argv[1])

hashType = (getattr(hashlib,str(sys.argv[3])))

print("Processing word list into hashed word list...")
# Run through word list, and create hashed dictionary
with open(sys.argv[1], encoding='utf8', errors='ignore') as openedFile:
#with open(sys.argv[1]) as openedFile:
        for line in openedFile:
            line = line.encode('utf-8').rstrip()
            hashObject = hashType(line)
            hashed = hashObject.hexdigest()
            dictionary.update({hashed:line})
print("Processed word list into hashed word list...")

print("Building hash list from hashes...")
# Create Counter, and add hashes to list
counter=0
with open(sys.argv[2]) as temphashList:
        for line in temphashList:
            if not line.startswith('00000'):
                line = line.rstrip()
                hashList.append(line)
print("Built hash list from hashes.")

print("Iterating through hash list, and comparing against word list...")
# Iterate through word list and compare to hash list
for hash in hashList:
    if hash in dictionary:
        print("*** MATCH- %s %s" % (hash, dictionary.get(hash)))
        counter +=1

print("Processing Complete...")
print("List had:", counter, "matches")
