import random 
from module import*

def ubah_candi(pasir, batu, air, list_candi, sumcandi, nama):
    if sumcandi == 1:
        id = 1
    else:
        id = sumcandi-1
    return updateDataList5 (id, nama , pasir, batu, air, list_candi,sumcandi) 

def bangun_candi(bahan, candi, jumlah_candi,nama):

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
        
        candi = ubah_candi(pasir, batu, air, candi, jumlah_candi, nama)
        jumlah_candi += 1
        print(f"Sisa candi yang perlu dibangun: {100 - jumlah_candi+2}.")
        print(candi)
        return candi, jumlah_candi


