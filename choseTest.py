from choseLeader import choseLeader, combin
from pprint import pprint
import optGoodLeader
import sys, random
def createArray(f, n):
    fault = random.sample(range(n),f)
    Lst = [0 for i in range(n)]
    for i in range(len(Lst)):
        if i in fault:
            Lst[i] = 1
    return Lst
        
def randChose(f, array, retryTimes):
    success = 0
    n = 3*f+1
    for i in range(retryTimes):
        chose = random.sample(range(n),f+1)
        Lst = [ array[i] for i in chose ]
        if sum(Lst)==0:
            success += 1
    print ('(success,retryTimes):',success,retryTimes)
    return float(success)/float(retryTimes) 

def smartChose(f, array, retryTimes):
    success = 0
    n = 3*f+1
    lastChose = []
    for i in range(retryTimes):
        if i==0:
            chose = random.sample(range(n),f+1)
            Lst = [ array[i] for i in chose ]
            if sum(Lst)==0:
                success += 1
            lastChose = Lst
        else:
            restLst = [ i for i in range(n) if i not in lastChose ]
            chose = random.sample(restLst, f+1)
            Lst = [ array[i] for i in chose ]
            if sum(Lst)==0:
                success += 1
    print ('(success,retryTimes)',success,retryTimes)
    return float(success)/float(retryTimes)

def main():
    array = createArray(int(sys.argv[1]), int(sys.argv[2]))
    print (randChose(int(sys.argv[1]) ,array, 10000))
    print (smartChose(int(sys.argv[1]), array, 10000))

if __name__=='__main__':
    main()
