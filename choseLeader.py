#!/usr/bin/env python3
from math import factorial
from pprint import pprint
import sys, os
import matplotlib.pyplot as plt

# will return combination a chose b
def combin(a, b):
    return factorial(a)/(factorial(a-b)*factorial(b))
# will return the probibility of f+1 good leader chosing
def choseLeader(faultNodes, n=None):
    f = faultNodes
    if n==None:
        n = 3*f+1
    if n<=(3*f):
        print ("n less than 1/3 f")
        return False
    Lst = [combin(f,i)*combin(n-f,f+1-i)/combin(n,f+1) for i in range(f+1)]
    #printResults(Lst)
    return Lst
# will print the input data with the predefined format
def printResults(dataLst):
    for i in range(len(dataLst)):
        print ("chose:",i,"fault leader")
        print ("the probility is:",dataLst[i])
        print ("=======================================")
# will plot the input data as a line chart base on the amounts of fault nodes 
def plotResults(faultNodes):
    # generate the plot input format
    f = faultNodes
    n = 3*f+1
    Lst = [[] for i in range(f+1)]
    for nodes in range(n,100):
        tmpLst = choseLeader(f, nodes)
        #print ("nodes amounts:",nodes,"\n",tmpLst,"\n================")
        for line in range(len(tmpLst)):
            Lst[line].append((nodes, tmpLst[line]))
    #pprint (Lst)
    # start to draw the plot
    for line in range(len(Lst)):
        x = [p[0] for p in Lst[line]]
        y = [p[1] for p in Lst[line]]
        plt.title("fault nodes amounts:"+str(f))
        plt.xlabel("Total nodes amounts")
        plt.ylabel("Probility")
        plt.xlim(0, 100)
        plt.ylim(0,1)
        plt.plot(x, y, "-", label="fault leader:%d"%(line,))
        plt.legend()
    # save the result
    os.makedirs("data", exist_ok=True)
    plt.savefig("data/{}faultNodes.png".format(f))
    # show the result
    plt.show()

# the entry point of the program
def main():
    if (len(sys.argv)<2):
        print ("There's no input parameters")
        sys.exit(1)
    try:
        if sys.argv[1]!="--plot":
            Lst = choseLeader(int(sys.argv[1]), int(sys.argv[2]))
        else:
            Lst = choseLeader(int(sys.argv[2]), int(sys.argv[3]))
            plotResults(len(Lst)-1)
    except IndexError:
        if sys.argv[1]!="--plot":
            Lst = choseLeader(int(sys.argv[1]))
        else:
            Lst = choseLeader(int(sys.argv[2]))
            plotResults(len(Lst)-1)

if __name__=="__main__":
    main()
