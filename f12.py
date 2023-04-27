from module import Bacafile

def ayamberkokok():
    f = Bacafile("candi.csv")
    jumlah = 0

    for line in f:
        jumlah += 1

    if jumlah < 100:
        print("Kukuruyuuk")
        print("Jumlah candi : ", jumlah)
        print("Roro Jonggrang dikutuk menjadi batu")
    else:
        print("Kukuruyuuk")
        print("Jumlah candi : ", jumlah)
        print("Bandung Bondowoso menang")