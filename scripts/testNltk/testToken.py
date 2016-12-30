'''
Created on Dec 30, 2016

@author: dexter
'''
#!/usr/bin/python

import argparse
import nltk
import re

parser = argparse.ArgumentParser(__file__, description="NLTK tester")

parser.add_argument("--input", "-i", dest='inputFile', help="Input a file" )
args = parser.parse_args()
fname=args.inputFile

with open(fname) as f:
    content = f.readlines()

logPattern="(.*?)\s(\d.*-\d.*-\d.*.*?)-(.*)"


for st in content:
    print ("working on:"+st)
    matchObj=re.match(logPattern, st)
    
    if matchObj:
        type = matchObj.group(1)
        date=matchObj.group(2)
        details = matchObj.group(3)
        print ("'", type.strip(),"'")
        print ("'", date.strip(),"'")
        print ("'", details.strip(),"'")
    else:
        print ("No match!!")
    print("\n")
    #tokens = nltk.word_tokenize(st)
    #print (tokens)