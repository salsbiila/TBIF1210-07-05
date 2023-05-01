from module import *

def hancurkancandi(datalist, datasum):
    A = input("Masukkan id candi yang akan dihapus: ")

    bool = False
    for i in range(datasum-1):
        if datalist[i][0] == A:
            bool = True
    
    if bool == True:
        B = input("Apakah yakin akan menghancurkan canid ini? (Y/N) ")
        if B == "Y":
            newdatalist = ["" for i in range(datasum - 1)]

            for i in range(datasum-1):
                if datalist[i][0] != A:
                    newdatalist = datalist[i][0]
                return newdatalist
        
        else:
            return datalist
    else:
        print("Id candi tidak ditemukan")
        return datalist