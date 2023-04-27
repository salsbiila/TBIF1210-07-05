from module import Bacafile, uang, maxmin, pisah, leng, ubah, ppop

global data, jumlahcandi, listharga

data = Bacafile("candi.csv")
jumlahCandi = -1
toPas = 0
toAir = 0
toBat = 0
listharga = ""
c = 0

for line in data:
    jumlahCandi += 1
    linedata = pisah(ubah(line, "\n", ""), ",")
    if c > 0:
        toPas += int(linedata[2])
        toAir += int(linedata[4])
        toBat += int(linedata[3])
        listharga += str(int(linedata[2]) * 1000 + int(linedata[3]) * 15000 + int(linedata[4]) * 7500) + ","
    c += 1

def jumlahcandi():
    return jumlahCandi

def laporancandi():
    data = Bacafile("candi.csv")
    c = 0
    idmax = 0
    Listharga = pisah(ppop(listharga), ",")

    for line in data:
        linedata = pisah(ubah(line, "\n", ""), ",")
        if c > 0:
            if jumlahCandi > 0:
                harga = int(linedata[2]) * 1000 + int(linedata[3]) * 15000 + int(linedata[4]) * 7500
                if harga == maxmin(Listharga)[0]:
                    maxharga = harga
                    idmax = linedata[0]
                elif harga == maxmin(Listharga)[1]:
                    minharga = harga
                    idmin = linedata[0]
            else:
                idmax = "-"
                idmin = "-"
                maxharga = 0
                minharga = 0
        c += 1
    print(f"Total Candi: {jumlahCandi}\nTotal Pasir yang digunakan: {toPas}\nTotal Batu yang digunakan: {toBat}\nTotal Air yang digunakan: {toAir}\nID Candi Termahal: {idmax} (Rp {uang(str(maxharga))})\nID Candi Termurah: {idmin} (Rp {uang(str(minharga))})")
laporancandi()