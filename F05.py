from module import *
from F03 import *

def ubahJin(dataSum, dataList):
    uname = input('Masukkan username jin : ')

    isProcessed = unameExists(uname, dataSum, dataList)

    if isProcessed:
        for i in range(1, dataSum):
            if dataList[i][0] == uname:
                row = i
        
        if dataList[row][2] == 'jin_pengumpul':
            userInput = input(f'Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
            
            if userInput == 'Y':
                newDataList = switchRole(row, dataSum, dataList)
            
        elif dataList[row][2] == 'jin_pembangun':
            userInput = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')

            if userInput == 'Y':
                newDataList = switchRole(row, dataSum, dataList)

        print()
        print('Jin telah berhasil diubah.')
        
        return newDataList

    else:
        print()
        print('Tidak ada jin dengan username tersebut.')

        return dataList