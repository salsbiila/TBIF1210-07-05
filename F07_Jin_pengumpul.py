import random 
def kumpul_candi(bahan, datasum):
    pasir = random.randint (0,5)
    batu = random.randint (0,5)
    air = random.randint (0,5)

    if datasum == 2:
        bahan = [['nama', 'deskripsi', 'jumlah'], ['pasir', 'deskripsi', 0], ['batu', 'deskripsi', 0], ['air', 'deskripsi', 0]]
    

    bahan [1][2] += pasir  
    bahan [2][2] += batu  
    bahan [3][2] += air
    print(f"Jin menemukan {pasir} pasir,  {batu} batu , dan  {air} air.")

    return bahan