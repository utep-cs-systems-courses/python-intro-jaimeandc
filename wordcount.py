#! /usc/bin/env python3
import sys
import os
import re

inputfile = sys.argv[1]
outputfile = sys.argv[2]

if len(sys.argv) is not 3:
    print("Correct Usage $python3 wordcount.py <your text file> <your output file>")
    exit()

 
input_text = open(inputfile,'r')
word_Dict = dict()
outtext = dict()

if not os.path.exists(inputfile):
    print("No Input file of that name exists")
    exit()

if not os.path.exists(outputfile):
    print("No Outputfile of that name exists")
    exit()

for line in input_text:
    line = line.strip()
    line = line.lower()
    line = re.sub(r'[^\w\s]',' ',line)
    words = line.split(" ")

    for word in words:
        if word in word_Dict:
            word_Dict[word] = word_Dict[word] + 1
        else:
            word_Dict[word] = 1
            
## Open and write onto file
out = open(outputfile, 'w')
for key, value in sorted(word_Dict.items(), key = lambda x: x[1], reverse=True):
    out.write(str(key) + ' ' + str(value) + '\n')

    
##Close Files
input_text.close()
out.close()
    

