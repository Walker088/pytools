#!/usr/bin/env python3
from math import factorial
import sys

# will return combination a chose b
def combination(a, b):
    return factorial(a)/(factorial(a-b)*factorial(b))
# will return the probibility of f+1 good leader chosing
def choseLeader(faultNodes, n=None):
    f = faultNodes
    if n==None:
        n = 3*f+1
    if n<=(3*f):
        print ("n less than 1/3 f")
        return False
    for i in range(f+1):
        P=combination(f,i)*combination(n-f,f+1-i)/combination(n,f+1)
        print ("Chose:",i,"fault leader")
        print ("The Probility is:", P,"\n")
# the entry point of the program
def main():
    if (len(sys.argv)<2):
        print ("There's no input parameters")
        sys.exit(1)
    try:
        choseLeader(int(sys.argv[1]), int(sys.argv[2]))
    except IndexError:
        choseLeader(int(sys.argv[1]))

if __name__=="__main__":
    main()
