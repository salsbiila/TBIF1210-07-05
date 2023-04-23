from F03 import *

file = open('user.csv', 'r')
userData = file.read()
userDataList = makeList(userData)

def hapusJin():
    uname = input('Masukkan username jin :')
    if unameExists(uname):
        userInput = input('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ')
        if userInput == 'Y':
            print()
    else:
        print('Tidak ada jin dengan username tersebut.')