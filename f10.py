from module import *

def Harga(pasir,batu,air):
    return pasir*1000 + batu*15000 + air*7500

def laporancandi(datafile, datasum):
    toPas = 0
    toBat = 0
    toAir = 0
    harga = 0
    if datasum == 2:
        idmax = '-'
        idmin = "-"
        maxharga = 0
        minharga = 0
    else:
        max = 0
        min = Harga(int(datafile[1][2]), int(datafile[1][3]), int(datafile[1][4]))

        for i in range(1, datasum - 1):
            harga = Harga(int(datafile[1][2]), int(datafile[1][3]), int(datafile[1][4]))
            if harga > max:
                maxharga = harga
                idmax = int(datafile[i][0])
            if harga < min:
                minharga = harga
                idmin = int(datafile[i][0])
            toPas += int(datafile[i][2])
            toBat += int(datafile[i][3])
            toAir += int(datafile[i][4])
    print("Total Candi:", (datasum - 1),"\nTotal Pasir yang digunakan: ",(toPas),"\nTotal Batu yang digunakan: ",(toBat),"\nTotal Air yang digunakan: ",(toAir),"\nID Candi Termahal: ",(idmax)," (Rp ",(uang(str(maxharga))),"\nID Candi Termurah: ",(idmin)," (Rp ",(uang(str(minharga))))