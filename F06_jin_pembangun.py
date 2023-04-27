import random 
def bangun_candi():
    pasir = random.randint (1,5)
    batu = random.randint (1,5)
    air = random.randint (1,5)
    if pasir <= bahan [1][2] and batu <= bahan [2][2] and air <= bahan [3][2]:
        bahan [1][2] -= pasir  
        bahan [2][2] -= batu  
        bahan [3][2] -= air
        rewrite_data("bahan_bangunan.csv", bahan)
        saveCandi(username, pasir, batu, air)
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {100-(command.length(candi))}.")