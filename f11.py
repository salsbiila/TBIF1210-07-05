from module import Bacafile, pisah, pan, leng, ubah

def hancurkancandi():
    c = Bacafile("candi.csv")
    A = input()
    M = ""

    for line in c:
        linedata = pisah(ubah(line, "\n", ""), ",")
        if linedata[0] != A:
            M += line

    c1 = open("candi.csv", "w")
    with open("candi.csv", "w") as file:
        file.write(M)
hancurkancandi( )