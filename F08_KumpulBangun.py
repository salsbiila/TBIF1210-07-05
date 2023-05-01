import random
from module import*

def kumpul(bahan, bahanDataSum, user, jumlah_user):
    jumlah_jin_pengumpul = 0
    # cek jumlah jin pengumpul
    for i in range(jumlah_user):
        if user[i][2] == 'jin_pengumpul' :
            jumlah_jin_pengumpul += 1
    print("ini jumlah jin pengumpul", jumlah_jin_pengumpul)

    hasil_kumpul= [0,0,0]
    for i in range (jumlah_jin_pengumpul):
        pasir = random.randint (0,5)
        batu = random.randint (0,5)
        air = random.randint (0,5)
        hasil_kumpul [0]+= pasir
        hasil_kumpul [1]+= batu
        hasil_kumpul [2]+= air

    if bahanDataSum == 2:
        bahan = [['nama', 'deskripsi', 'jumlah'], ['pasir', 'deskripsi', 0], ['batu', 'deskripsi', 0], ['air', 'deskripsi', 0]]

    # tambahin ke bahan
    bahan[1][2] = int()
    bahan[2][2] = int()
    bahan[3][2] = int()

    bahan [1][2] += hasil_kumpul[0]
    bahan [2][2] += hasil_kumpul[1]
    bahan [3][2] += hasil_kumpul[2]

    if jumlah_jin_pengumpul != 0:
        print (f'Mengerahkan {jumlah_jin_pengumpul} jin untuk mengumpulkan bahan.')
        print (f'Jin menemukan total {hasil_kumpul [0]} pasir, {hasil_kumpul [1]} batu, dan {hasil_kumpul [2]} air.') 
    else :
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
    
    return bahan

def saveCandiF8(username, pasir, batu, air, sumcandi, list_candi):
    if sumcandi == 2:
        id = 1
    else:
        id = int(list_candi[sumcandi - 2][0]) + 1
    return updateDataList5 (id, username, pasir, batu, air, sumcandi, list_candi)

def bangun(bahan, candi, jumlah_candi, user, jumlah_user):
    jumlah_jin_pembangun = 0
    # cek jumlah jin pembangun
    for i in range(jumlah_user):
        if user[i][2] == 'jin_pembangun':
            jumlah_jin_pembangun += 1
    
    # jumlah_candi = 0
    # # cek jumlah candi
    # for i in range(jumlah_candi):
    #     if user[i][2] != '':
    #         jumlah_candi += 1
    
    # dapatkan username
    username = ['' for i in range(jumlah_jin_pembangun)]
    idx_user = 0
    for i in range(jumlah_user):
        if user[i][2] == 'jin_pembangun':
            username[idx_user] = user[i][0]
            idx_user += 1

    # ubah tipe jadi int
    hasil_candi = [[0, 0, 0] for i in range(jumlah_jin_pembangun)] # dapatkan bahan tiap candi
    print("Mengerahkan", jumlah_jin_pembangun, "untuk membangun candi dengan total bahan")
    if jumlah_jin_pembangun > 0:
        for i in range (jumlah_jin_pembangun):
            hasil_bangun = [0,0,0]
            pasir = random.randint (1,5)
            batu = random.randint (1,5)
            air = random.randint (1,5)
            hasil_bangun [0]+= pasir
            hasil_bangun [1]+= batu
            hasil_bangun [2]+= air

            hasil_candi [i][0] = pasir
            hasil_candi [i][1] = batu
            hasil_candi [i][2] = air
        print("Mengerahkan ", jumlah_jin_pembangun, " untuk membangun candi dengan total bahan ", hasil_bangun [0], " pasir, ", hasil_bangun [1], "batu, dan ", hasil_bangun[2], "air.")
        if hasil_bangun [0]<= bahan [1][2] and hasil_bangun[1] <= bahan [2][2] and hasil_bangun[2] <= bahan [3][2]:
                # kurangin bahan
            bahan [1][2] -= hasil_bangun[0]
            bahan [2][2] -= hasil_bangun[1]
            bahan [3][2] -= hasil_bangun[2]

                # simpan candi
            jumlahcandi = 0
            for i in range(jumlah_jin_pembangun):
                candi = saveCandiF8(username[i], hasil_candi[i][0], hasil_candi[i][1], hasil_candi[i][2], jumlah_candi, candi)
                jumlah_candi += 1
                jumlahcandi += 1
            print("Jin berhasil membangun ", jumlahcandi, " buah candi.")
            return candi, jumlah_candi
        else:
            print("bahan tidak cukup, kumpulkan lagi bahan")
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
    return candi, jumlah_candi