import random
def kumpul():
    jumlah_jin_pengumpul = 0 #asumsi sudah ada jumlah jinpengumpul
    hasil_kumpul= [0,0,0]
    for i in range (jumlah_jin_pengumpul):
        pasir = random.randint (0,5)
        batu = random.randint (0,5)
        air = random.randint (0,5)
        hasil_kumpul [0]+= pasir
        hasil_kumpul [0]+= batu
        hasil_kumpul [0]+= air
    if jumlah_jin_pengumpul != 0:
        print (f'Mengerahkan {jumlah_jin_pengumpul} jin untuk mengumpulkan bahan.')
        print (f'Jin menemukan total {hasil_kumpul [0]} pasir, {hasil_kumpul [1]} batu, dan {hasil_kumpul [2]} air.') 
    else :
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
def bangun(bahan, saveCandi):
    jumlah_jin_pembangun = 0 #asumsi sudah ada jin pembangun
    hasil_bangun = [0,0,0]
    for i in range (jumlah_jin_pembangun):
        pasir = random.randint (0,5)
        batu = random.randint (0,5)
        air = random.randint (0,5)
        hasil_bangun [0]+= pasir
        hasil_bangun [0]+= batu
        hasil_bangun [0]+= air
    if hasil_bangun [0]<= bahan[0] and hasil_bangun[1] <= bahan [1] and hasil_bangun[2] <= bahan [2]:
        saveCandi ()
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')














