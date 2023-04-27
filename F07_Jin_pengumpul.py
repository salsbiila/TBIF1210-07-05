import random 
def kumpul_candi():
    pasir = random.randint (1,5)
    batu = random.randint (1,5)
    air = random.randint (1,5)  
    bahan [1][2] += pasir  
    bahan [2][2] += batu  
    bahan [3][2] += air
    print(f"Jin menemukan {pasir} pasir,  {batu} batu , dan  {air} air.")