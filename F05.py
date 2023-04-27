from module import *
from F03 import *

def ubahJin(dataSum, dataList):
    uname = input('Masukkan username jin : ')

    isProcessed = unameExists(uname, dataSum, dataList)
    print(isProcessed)

    if isProcessed:
        for i in range(1, dataSum):
            if dataList[i][0] == uname:
                idx = i
        
        if dataList[idx][2] == 'jin_pengumpul':
            userInput = input(f'Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
            
            if userInput == 'Y':
                dataList[idx][2] = 'jin_pembangun'

                print('Jin telah berhasil diubah .')

        elif dataList[idx][2] == 'jin_pembangun':
            userInput = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')

            if userInput == 'Y':
                dataList[idx][2] = 'jin_pengumpul'

                print('Jin telah berhasil diubah.')
    else:
        print('Tidak ada jin dengan username tersebut.')
