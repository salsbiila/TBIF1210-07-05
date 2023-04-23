from module import *
import time

file = open('user.csv', 'r')
userData = file.read()
userDataList = makeList(userData)
dataSum = rowCount(userData)

def unameExists(uname, data = userDataList):    # fungsi untuk mengecek apakah username sudah ada atau belum
    for i in range(1, dataSum):
        if data[i][0] == uname:
            return True
    return False

def jinAccount(data):   # fungsi yang menghandle pembuatan akun
    uname = input('Masukkan username jin: ')
    while unameExists(uname, data):
        print(f'Username “{uname}” sudah diambil!')
        uname = input('Masukkan username jin: ')
    
    password = input('Masukkan password jin: ')
    while len(password) < 5 or len(password) > 25:
        print('Password panjangnya harus 5-25 karakter!')
        password = input('Masukkan password jin: ')
    
    print('Mengumpulkan sesajen...')
    time.sleep(1)
    print('Menyerahkan sesajen...')
    time.sleep(1)
    print('Membacakan mantra...')
    time.sleep(1)

    print(f'Jin {uname} berhasil dipanggil!')

    return uname, password

def summonJin(data = userDataList):
    if dataSum == 103:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
        print(' (2) Pembangun - Bertugas membangun candi')

        jinType = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))

        while jinType != 1 and jinType != 2:
            print(f'Tidak ada jenis jin bernomor “{jinType}”!')

            jinType = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
        
        if jinType == 1:
            print('Memilih jin “Pengumpul”.')
            uname, password = jinAccount(data)
            newDataList = updateDataList3(uname, password, 'jin_pengumpul', userDataList)
            newDataStr = updateData3(uname, password, 'jin_pengumpul')

            return newDataList, newDataStr

        elif jinType == 2:
            print('Memilih jin “Pembangun”.')
            uname, password = jinAccount(data)
            newDataList = updateDataList3(uname, password, 'jin_pembangun', userDataList)
            newDataStr = updateData3(uname, password, 'jin_pembangun')

            return newDataList, newDataStr