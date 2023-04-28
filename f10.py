from module import *

global data, jumlahcandi, listharga


def harga(pasir,batu,air):
    return pasir*1000 + batu*15000 + air*7500

def laporancandi(datafile, datasum):
    toPas, toBat, toAir = 0
    if datasum == 1:
        idmax, idmin = "-"
    else:      
        max = 0
        min = harga(int(datafile[1][2]), int(datafile[1][3]), int(datafile[1][4]))
        Listharga = pisah(ppop(listharga), ",")

        for i in range(1, datasum - 1):
            harga = harga(int(datafile[1][2]), int(datafile[1][3]), int(datafile[1][4]))
            if harga > max:
                maxharga = harga
                idmax = datafile[i][0]
            if harga < min:
                minharga = harga
                idmin = datafile[i][0]
            toPas += datafile[i][2]
            toBat += datafile[i][3]
            toAir += datafile[i][4]
    print(f"Total Candi: {datasum - 1}\nTotal Pasir yang digunakan: {toPas}\nTotal Batu yang digunakan: {toBat}\nTotal Air yang digunakan: {toAir}\nID Candi Termahal: {idmax} (Rp {uang(str(maxharga))})\nID Candi Termurah: {idmin} (Rp {uang(str(minharga))})")