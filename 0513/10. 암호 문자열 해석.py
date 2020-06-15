# 10. string -> 숫자

def getnum(b):
    srcList = list(b) #list(): string->list
    for i in range(len(srcList)):
        srcList[i] = ord(srcList[i])
    return srcList

print(getnum('Hello'))