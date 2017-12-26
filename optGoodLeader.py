from choseLeader import choseLeader
from choseLeader import combin
from pprint import pprint
def compareDis(faultNodes, n=None):
# will return the best distribution of leader chosing after the first round
    f = faultNodes
    if n==None:
        n = 3*f+1
    if n<=(3*f):
        print ('nless than 1/3 f')
    
    # starting calculating
    # 1. calculating all the possible distribution and their possibilities
    faultPosLst = []
    chosedLst = choseLeader(f, n)
    for faultPos in range(1, len(chosedLst)):
        Lst = [[(i,f+1-i),(combin(faultPos,0)*combin(f+1-faultPos,i)/combin(f+1,i)) * (combin(f-faultPos,0)*combin(n-2*f-1+faultPos,f+1-i)/combin(n-f-1,f+1-i))] for i in range(f+2) if (f+1-faultPos)>=i]
        faultPosLst.append(Lst)
    #pprint (faultPosLst)

    # 2. adding the frist chosing posibilities to each result
    # then chose the best distribution of next round leader set chosing
    percentLst = [ chosedLst[i]/sum(chosedLst[1:]) for i in range(1,len(chosedLst)) ]
    #resultLst  = [ persentLst[i]*faultPosLst[] ]
    for faultPos in range(len(faultPosLst)):
        for choseDis in range(len(faultPosLst[faultPos])):
        #print (faultPosLst[faultPos][1]) 
        #print (chosedLst[faultPos+1])
            #print (faultPosLst[faultPos][choseDis])
            faultPosLst[faultPos][choseDis][1] *= percentLst[faultPos]
    pprint (faultPosLst)

    # 3. calculating the possibilities of the rest of new chosedLst
    resultDic = {}
    for chose in range(f+1):
        resultDic[str(chose)+','+str(f-chose+1)] = 0
    print (resultDic)
def plotResult():
    pass

def main():
    compareDis(3)
if __name__=='__main__':
    main()
