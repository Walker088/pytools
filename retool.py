#!/usr/bin/env python

#The projet is written with py3
#Using to compare several patterns
#by regular expression
import sys
import re

def main():
    if (len(sys.argv)<2):
        print ('There\'s no input string or files')
        sys.exit(1)
    isPhoneNumber(sys.argv[1])

def isPhoneNumber(argv1):
    fileRegex = re.compile(r'^\w+\.\w+$')
    numberRegex = re.compile(r'')
    isFile = fileRegex.search(argv1)
    if (isFile != None):
        print ('it\'s a file:',isFile.group())
        with open ('resrc/'+argv1,'r') as f:
            contentsLst = f.readlines()
            results = [number for number in contentsLst if numberRegex.search(number)!=None]
            with open ('resrc/result.txt','w') as outf:
                for item in results:
                    outf.write(item)
    else:
        print ('it\'s a string:',argv1)
def isEmailAddr(argv1):
    pass

if __name__=="__main__":
    main()
