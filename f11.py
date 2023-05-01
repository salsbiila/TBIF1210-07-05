from module import *

def hancurkancandi(datalist):
    c = Bacafile("candi.csv")
    A = input()
    M = ""
    i = 0

    for line in c:
        if datalist[i][0] != A:
            M += line
        i += 1
    newdatalist = makeList(M)
    return newdatalist