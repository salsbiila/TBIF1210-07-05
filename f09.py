from module import Bacafile, maxmin, pisah, leng, ubah, pan
from f10 import jumlahcandi

Urutanleksikal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
j = Bacafile("candi.csv")
c = Bacafile("bahan_bangunan.csv")
d = Bacafile("user.csv")
jumlahJin = -1
jinPembangun = 0
count = 0

A = ["" for x in range(jumlahcandi())]

for line in j:
    linedata = pisah(ubah(line, "\n", ""), ",")
    if count > 0 :
        A[count - 1] = linedata[1]
    count += 1

for i in range(leng(A)):
    max = 0
    if pan(A,A[i]) > max:
        print("A")
        max = pan(A,A[i])
        jinTrajin = A[i]

for i in A:
    min = max
    if pan(A,i) < min:
        min = pan(A,i)
        jinPmalas = i

jinPembangun = leng(A)
for i in A:
    jinPembangun -= pan(A,i) - 2

jinPengumpul = jumlahJin - jinPembangun

count = 0

for line in c:
    linedata = pisah(ubah(line, "\n", ""), ",")
    if count == 1:
        jumlahPasir = int(linedata[2])
    elif count == 2:
        jumlahAir = int(linedata[2])
    elif count == 3:
        jumlahBatu = int(linedata[2])
    count += 1
 
jinPengumpul = jumlahJin - jinPembangun
print(f"Total jin : {jumlahJin}")
print(f"Total jin pengumpul : {jinPengumpul}")
print(f"Total jin pembangun : {jinPembangun}")
print(f"Jin terajin : {jinTrajin}")
print(f"Jin pemalas : {jinPmalas}")
print(f"Jumlah pasir : {jumlahPasir}")
print(f"Jumlah air : {jumlahAir}")
print(f"Jumlah batu : {jumlahBatu}")