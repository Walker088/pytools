import sys

def titleTransfer(Lst):
    return [string.title() for string in Lst]

if __name__=="__main__":
    Lst=['AAADCDE DJIJI SDKJFIA',
        'EJCLKMVADJFI DIJJFAKLDJF DIJFALKDJ',
        'QQIEJRIKEJKC DDQHUE AFLKDJF']
    resLst=titleTransfer(Lst)
    print ('result: ',resLst)
    with open('result.txt','w') as outfile:
        for string in resLst:
            outfile.write(string+'\n')
