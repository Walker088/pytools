#!/usr/bin/env python3
from choseLeader import choseLeader
from choseLeader import combin
from pprint import pprint
import sys

def calAllPos(n, chosedLst):
    # 1. calculating all the possible distribution and their possibilities
    faultPosLst = []
    f = len(chosedLst)-1
    for faultPos in range(1, len(chosedLst)):
        Lst = [[(i,f+1-i),(combin(faultPos,0)*combin(f+1-faultPos,i)/combin(f+1,i)) * (combin(f-faultPos,0)*combin(n-2*f-1+faultPos,f+1-i)/combin(n-f-1,f+1-i))] for i in range(f+2) if (f+1-faultPos)>=i]
        faultPosLst.append(Lst)
    return faultPosLst
def calBestPar(faultPosLst, chosedLst):
    # 2. adding the frist chosing posibilities to each result
    # then chose the best distribution of next round leader set chosing
    percentLst = [ chosedLst[i]/sum(chosedLst[1:]) for i in range(1,len(chosedLst)) ]
    compareLst = [ 0 for i in range(len(faultPosLst[0])) ]
    for faultPos in range(len(faultPosLst)):
        for choseDis in range(len(faultPosLst[faultPos])):
            faultPosLst[faultPos][choseDis][1] *= percentLst[faultPos]
    for i in range(len(faultPosLst)):
        for j in range(len(faultPosLst[0])):
            try:
                compareLst[j] += faultPosLst[i][j][1]
            except IndexError:
                pass
    return compareLst
def choseResult(compareLst):
    for i in range(len(compareLst)):
        if compareLst[i]==max(compareLst):
            chose = i
            break
    return chose   
def calRestPos(chosedLst, chose):
    # 3. calculating the possibilities of the rest of new chosedLst
    percentLst = [ chosedLst[i]/sum(chosedLst[1:]) for i in range(1,len(chosedLst)) ]
    newChosedLst = [ [] for i in range(len(chosedLst)-1) ]
    f = len(chosedLst)-1
    n = 3*f+1
    l = chose
    r = f+1-l
    for faultNum in range(len(newChosedLst)):
        for faultPos in range(len(chosedLst)):
            try:
                newChosedLst[faultNum].append( (combin(faultNum+1,l)*combin(f-faultNum,l)/combin(f+1,l)) * (combin(n-2*f+faultNum,r-faultPos)*combin(f-faultNum-1,faultPos)/combin(n-f-1,r)) )
            except ValueError:
                newChosedLst[faultNum].append(0)
                continue
    for faultNum in range(len(newChosedLst)):
        for faultPos in range(len(newChosedLst[faultNum])):
            newChosedLst[faultNum][faultPos] *= percentLst[faultNum]
    resultLst = [ 0 for i in range(len(newChosedLst[0])) ]
    for i in range(len(newChosedLst[0])):
        for j in range(len(newChosedLst)):
            resultLst[i] += newChosedLst[j][i]
    return resultLst

def compareDis(chosedLst,f,n=None):
# will return the best distribution of leader chosing after the first round
    if n==None:
        n = 3*f+1
    faultPosLst = calAllPos(n, chosedLst)
    compareLst = calBestPar(faultPosLst, chosedLst)
    chose = choseResult(compareLst)
    return calRestPos(chosedLst, chose) 

def plotResult():
    pass

def main():
    faultNodes = int(sys.argv[1])
    chosedLst = choseLeader(faultNodes)
    for i in range(10):
        if i==0:
            newChosedLst = compareDis(chosedLst, faultNodes)
            print (newChosedLst)
        else:
            newChosedLst = compareDis(newChosedLst, faultNodes)
            print (newChosedLst)
if __name__=='__main__':
    main()
