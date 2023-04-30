from module import *

def laporanjin(datalistcandi, datalistbahan, datasumcandi, datalistuser, datasumuser, urutan):
    listjin = ["" for x in range((datasumcandi))]

    for i in range(1,datasumcandi - 1):
        listjin[i] = datalistcandi[i][1]

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
    for i in range(1, datasumuser - 1):
        if datalistuser[i][2] == "jin_pembangun":
            jinPembangun += 1
    jinPengumpul = jumlahjin - jinPembangun

    count = 0

    for line in datalistbahan:
        if count == 1:
            jumlahPasir = int(line[2])
        elif count == 2:
            jumlahAir = int(line[2])
        elif count == 3:
            jumlahBatu = int(line[2])
        count += 1
    
    print(f"Total jin : {datasumcandi - 1}")
    print(f"Total jin pengumpul : {jinPengumpul}")
    print(f"Total jin pembangun : {jinPembangun}")
    print(f"Jin terajin : {jinTrajin}")
    print(f"Jin pemalas : {jinPmalas}")
    print(f"Jumlah pasir : {jumlahPasir}")
    print(f"Jumlah air : {jumlahAir}")
    print(f"Jumlah batu : {jumlahBatu}")