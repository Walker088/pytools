from choseLeader import choseLeader, combin
from pprint import pprint
import optGoodLeader
import sys, random
import numpy as np
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
    #print ('(success,retryTimes):',success,retryTimes)
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
    #print ('(success,retryTimes)',success,retryTimes)
    return float(success)/float(retryTimes)

def Test100(f, n):
    randLst = []
    smartLst = []
    for arr in range(100):
        array = createArray(f, n)
        print ('finished array:',arr)
        for time in range(100):
            randPos = randChose(f, array, 1000)
            smartPos = smartChose(f, array, 1000)
            randLst.append(randPos)
            smartLst.append(smartPos)
    return analysis(np.asarray(randLst), np.asarray(smartLst))

def analysis(randLst, smartLst):
    randAv = sum(randLst)/len(randLst)
    randSd = np.std(randLst)
    smartAv = sum(smartLst)/len(smartLst)
    smartSd = np.std(smartLst)
    return {'random chose':{ 'average:':randAv, 'std:':randSd }, 'smart chose':{'average:':smartAv, 'std:':smartSd} }

def main():
#    array = createArray(int(sys.argv[1]), int(sys.argv[2]))
#    print (randChose(int(sys.argv[1]) ,array, 10000))
#    print (smartChose(int(sys.argv[1]), array, 10000))
    pprint (Test100(int(sys.argv[1]), int(sys.argv[2])))

if __name__=='__main__':
    main()
