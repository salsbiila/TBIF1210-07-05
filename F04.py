from module import *
from F03 import *

def hapusJin(userDataSum, userDataList, candiDataSum, candiDataList, role):
    if role == 'bandung_bondowoso':
        uname = input('Masukkan username jin : ')
        if unameExists(uname, userDataSum, userDataList):
            userInput = input('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ')
            if userInput == 'Y':
                newUserSum, newUserDataList = deleteUser(uname, userDataSum, userDataList)

                newCandiSum, newCandiDataList = deleteCandi(uname, candiDataSum, candiDataList)

                print()
                print('Jin telah berhasil dihapus dari alam gaib.')

                return newUserSum, newUserDataList, newCandiSum, newCandiDataList
        else:
            print()
            print('Tidak ada jin dengan username tersebut.')

            return userDataSum, userDataList, candiDataSum, candiDataList
    
    else:
        print("Pemain tidak memiliki kemampuan ini")

        return userDataSum, userDataList, candiDataSum, candiDataList