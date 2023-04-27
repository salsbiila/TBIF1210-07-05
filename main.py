from module import *
from F03 import *
from F05 import *

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

    if userInput == 'summonjin':
        userDataList, userData = summonJin(userDataSum, userDataList, userData)
        userDataSum += 1
    
    elif userInput == 'ubahjin':
        ubahJin(userDataSum, userDataList)
    
    elif userInput == 'q':  # blm selesai
        playing = False