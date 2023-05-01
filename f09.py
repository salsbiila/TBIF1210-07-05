from module import *

def laporanjin(datalistcandi, datalistbahan, datasumbahan, datasumcandi, datalistuser, datasumuser, urutan):
    listjin = ["" for x in range((datasumcandi))]

    for i in range(1,datasumcandi - 1):
        listjin[i] = datalistcandi[i][1]

    if datasumcandi == 2:
        jinTrajin = "-"
        jinPmalas = "-"
    else:
        for i in range(leng(listjin)):
            max = 0
            jinTrajin = "Z"
            if pan(listjin,listjin[i]) > max:
                max = pan(listjin,listjin[i])
                if cariIdx(urutan, listjin[i][0]) <= cariIdx(urutan, jinTrajin[0]):
                    jinTrajin = listjin[i]

        for i in range(leng(listjin)):
            min = max
            jinPmalas = "A"
            if pan(listjin,i) < min:
                min = pan(listjin,i)
                if cariIdx(urutan, listjin[i][0]) >= cariIdx(urutan, jinTrajin[0]):
                    jinPmalas = listjin[i]

    jinPembangun = 0
    jumlahjin = datasumuser - 3
    for i in range(1, datasumuser):
        if datalistuser[i][2] == "jin_pembangun":
            jinPembangun += 1
    jinPengumpul = jumlahjin - jinPembangun

    count = 0
    
    if datasumbahan == 2:
        jumlahAir = 0
        jumlahBatu = 0
        jumlahPasir = 0
    else:
        for line in datalistbahan:
            if count == 1:
                jumlahPasir = int(line[2])
            elif count == 2:
                jumlahAir = int(line[2])
            elif count == 3:
                jumlahBatu = int(line[2])
            count += 1
    
    print("Total jin : ",jumlahjin)
    print("Total jin pengumpul : ",jinPengumpul)
    print("Total jin pembangun : ",jinPembangun)
    print("Jin terajin : ", jinTrajin)
    print("Jin pemalas : ", jinPmalas)
    print("Jumlah pasir : ", jumlahPasir)
    print("Jumlah air : ", jumlahAir)
    print("Jumlah batu : ", jumlahBatu)