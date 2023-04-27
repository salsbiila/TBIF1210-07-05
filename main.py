from module import *
from F03 import *
from F04 import *
from F05 import *
from F16 import *

file = open('user.csv', 'r')
userData = file.read()
userDataList = makeList(userData)
userDataSum = rowCount(userData)

file = open('candi.csv', 'r')
candiData = file.read()
candiDataList = makeList(candiData)
candiDataSum = rowCount(candiData)

file = open('bahan_bangunan.csv', 'r')
bahanData = file.read()
bahanDataList = makeList(bahanData)
bahanDataSum = rowCount(bahanData)

# belum final belum dibenerin

playing = True

while playing:
    userInput = input('>>> ')

    if userInput == 'summonjin':    #F03
        userDataList = summonJin(userDataSum, userDataList)
        userDataSum += 1
    
    elif userInput == 'hapusjin':   #F04
        userDataSum, userDataList, candiDataSum, candiDataList = hapusJin(userDataSum, userDataList, candiDataSum, candiDataList)
    
    elif userInput == 'ubahjin':    #F05
        ubahJin(userDataSum, userDataList)
    
    elif userInput == 'exit':   #F16
        if exit():
            print('masuk ke f14')
        playing = False