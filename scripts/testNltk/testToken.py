'''
Created on Dec 30, 2016

@author: dexter
'''
#!/usr/bin/python

import argparse
import nltk
import re
import gzip
from  Models.SentenceModel import Sentence

parser = argparse.ArgumentParser(__file__, description="NLTK tester")

parser.add_argument("--input", "-i", dest='inputFile', help="Input a file" )
parser.add_argument("--output", "-o", dest='outputFile', help="Write to output file")

args = parser.parse_args()
fname=args.inputFile

with open(fname) as f:
    content = f.readlines()
#2016-12-30 16:27:54,435
#logPattern="(.*?)\s(\d.*?-\d.*?-\d.*?.*?)-(.*)"
logPattern="(.*?)\s*?(\d{4}-\d{2}-\d{2}[\s\t]*?\d{2}:\d{2}:\d{2}[\,\.]*?\d{3})\s*?(.*?$)"
#logPattern="(.*?)\s(\d{4}-\d{2}-\d{2}.*?\d{2}:\d{2}:\d{2}.*?)-(.*)"

ErrorSet=[]

for st in content:
    matchObj=re.match(logPattern, st)
    
    if matchObj:
        type = matchObj.group(1)
        date=matchObj.group(2)
        details = matchObj.group(3)
        ErrorSet.append(Sentence(details) )
    else:
        print ("No match!!")
    print("\n")


print ("do the comparison")

fo = open(args.outputFile,'w')

for i in range(0,len(ErrorSet)):
    print ("S"+str(i)+":"+ErrorSet[i].mystr)
    fo.write("S"+str(i)+":"+ErrorSet[i].mystr+"\n")

fo.write ("with Jaccord Distance:\n")
for i in range(0,len(ErrorSet)):
    for j in range (0,i+1):
       #compare the distance in matrix 
       dist = ErrorSet[i].calculateJaccardDist(ErrorSet[j])
       
       fo.write(str(dist))
       if( i==j):
           fo.write(";")
       else:
           fo.write(",")
    fo.write("\n")

fo.write ("with Measuring Agreement on Set-valued Items (MASI) Distance:\n")    
for i in range(0,len(ErrorSet)):
    for j in range (0,i+1):
       #compare the distance in matrix 
       dist = ErrorSet[i].calculateMasiDist(ErrorSet[j])
       
       fo.write(str(dist))
       if( i==j):
           fo.write(";")
       else:
           fo.write(",")
    fo.write("\n")
fo.close()