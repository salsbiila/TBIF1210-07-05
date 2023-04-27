from module import *
import time

def unameExists(uname, dataSum, dataList):    # fungsi untuk mengecek apakah username sudah ada atau belum
    for i in range(1, dataSum):
        if dataList[i][0] == uname:
            return True
    return False

def jinAccount(dataSum, dataList):   # fungsi yang menghandle pembuatan akun
    uname = input('Masukkan username jin: ')
    while unameExists(uname, dataSum, dataList):
        print()
        print(f'Username “{uname}” sudah diambil!')
        print()
        uname = input('Masukkan username jin: ')
    
    password = input('Masukkan password jin: ')
    print()
    while len(password) < 5 or len(password) > 25:
        print('Password panjangnya harus 5-25 karakter!')
        print()
        password = input('Masukkan password jin: ')
        print()
    
    print('Mengumpulkan sesajen...')
    time.sleep(1)
    print('Menyerahkan sesajen...')
    time.sleep(1)
    print('Membacakan mantra...')
    time.sleep(1)

    print()
    print(f'Jin {uname} berhasil dipanggil!')

    return uname, password

def summonJin(dataSum, dataList):
    if dataSum == 103:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
        print(' (2) Pembangun - Bertugas membangun candi')
        print()

        jinType = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
        print()

        while jinType != 1 and jinType != 2:
            print(f'Tidak ada jenis jin bernomor “{jinType}”!')
            print()

            jinType = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
            print()
        
        if jinType == 1:
            print('Memilih jin “Pengumpul”.')
            print()
            uname, password = jinAccount(dataSum, dataList)
            newDataList = updateDataList3(uname, password, 'jin_pengumpul', dataSum, dataList)

            return newDataList

        elif jinType == 2:
            print('Memilih jin “Pembangun”.')
            print()
            uname, password = jinAccount(dataSum, dataList)
            newDataList = updateDataList3(uname, password, 'jin_pembangun', dataSum, dataList)

            return newDataList