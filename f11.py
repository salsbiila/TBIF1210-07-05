from module import *

def hancurkancandi(datalist, datasum):
    A = input("Masukkan id candi yang akan dihapus: ")
    newdatalist = ["" for i in range(datasum - 1)]
    i = 0

    for i in range(datasum-1):
        if datalist[i][0] != A:
            newdatalist = datalist[i][0]
    return newdatalist