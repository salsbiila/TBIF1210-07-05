import random 
from module import*

def bangun_candi(bahan, candi, jumlah_candi):

    pasir = random.randint (1,5)
    batu = random.randint (1,5)
    air = random.randint (1,5)

    # ubah tipe jadi int
    bahan[1][2] = int(bahan[1][2])
    bahan[2][2] = int(bahan[2][2])
    bahan[3][2] = int(bahan[3][2])
    
    if pasir <= bahan [1][2] and batu <= bahan [2][2] and air <= bahan [3][2]:   
        print(f"Candi berhasil dibangun dengan {pasir} pasir, {batu} batu, {air} air")
        bahan [1][2] -= pasir  
        bahan [2][2] -= batu  
        bahan [3][2] -= air

        # append candi baru ke list candi
        candi = ubah_candi(pasir, batu, air, jumlah_candi, candi)
        jumlah_candi += 1
        print(f"Sisa candi yang perlu dibangun: {100 - jumlah_candi+2}.")
        print(candi)
        return candi, jumlah_candi


def ubah_candi(pasir, batu, air, x, y):
    id = 1 # tolong bikin id lagi. Karena harus berubah2 sama nama user saat ini
    return updateDataList5 (id, "ucok", pasir, batu, air, x,y) #cari cara update nya
