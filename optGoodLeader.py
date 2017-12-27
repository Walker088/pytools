#!/usr/bin/env python3
from choseLeader import choseLeader
from choseLeader import combin
from pprint import pprint
def compareDis(chosedLst,f,n=None):
# will return the best distribution of leader chosing after the first round
    # starting calculating
    # 1. calculating all the possible distribution and their possibilities
    if n==None:
        n = 3*f+1
    faultPosLst = []
    for faultPos in range(1, len(chosedLst)):
        Lst = [[(i,f+1-i),(combin(faultPos,0)*combin(f+1-faultPos,i)/combin(f+1,i)) * (combin(f-faultPos,0)*combin(n-2*f-1+faultPos,f+1-i)/combin(n-f-1,f+1-i))] for i in range(f+2) if (f+1-faultPos)>=i]
        faultPosLst.append(Lst)

    # 2. adding the frist chosing posibilities to each result
    # then chose the best distribution of next round leader set chosing
    percentLst = [ chosedLst[i]/sum(chosedLst[1:]) for i in range(1,len(chosedLst)) ]
    compareLst  = [ 0 for i in range(len(faultPosLst[0])) ]
    for faultPos in range(len(faultPosLst)):
        for choseDis in range(len(faultPosLst[faultPos])):
            faultPosLst[faultPos][choseDis][1] *= percentLst[faultPos]
    pprint (faultPosLst)
        
    for i in range(len(faultPosLst)):
        for j in range(len(faultPosLst[0])):
            try:
                compareLst[j] += faultPosLst[i][j][1]
            except IndexError:
                pass
                #print ('(i,j):',i,j)
    print (compareLst)

    chose = 0
    for i in range(len(compareLst)):
        if compareLst[i]==max(compareLst):
            chose = i
            break
    print ('chose:',chose)
    
    # 3. calculating the possibilities of the rest of new chosedLst
    resultLst = [ (combin()*combin()/combin()) * (combin()*combin()/combin()) for i in range(f+1)]
    return resultLst

def plotResult():
    pass

def main():
    faultNodes = 3
    chosedLst = choseLeader(faultNodes)
    compareDis(chosedLst, faultNodes)
if __name__=='__main__':
    main()
