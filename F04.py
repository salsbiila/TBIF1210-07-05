from module import *
from F03 import *

def hapusJin(userDataSum, userDataList, candiDataSum, candiDataList):
    uname = input('Masukkan username jin :')
    if unameExists(uname, userDataSum, userDataList):
        userInput = input('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ')
        if userInput == 'Y':
            newUserSum, newUserDataList = deleteUser(uname, userDataSum, userDataList)

            newCandiSum, newCandiDataList = deleteCandi(uname, candiDataSum, candiDataList)

            return newUserSum, newUserDataList, newCandiSum, newCandiDataList
    else:
        print('Tidak ada jin dengan username tersebut.')