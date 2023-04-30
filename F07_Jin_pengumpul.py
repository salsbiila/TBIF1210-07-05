import random 
def kumpul_candi(bahan):
    pasir = random.randint (0,5)
    batu = random.randint (0,5)
    air = random.randint (0,5)  

    # ubah tipe jadi int
    bahan[1][2] = int(bahan[1][2])
    bahan[2][2] = int(bahan[2][2])
    bahan[3][2] = int(bahan[3][2])

    bahan [1][2] += pasir  
    bahan [2][2] += batu  
    bahan [3][2] += air
    print(f"Jin menemukan {pasir} pasir,  {batu} batu , dan  {air} air.")