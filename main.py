from module import *
from F03 import *

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
while True:
    userInput = input('>>> ')

    if userInput == 'summonjin':
        userDataList, userData = summonJin()
        userDataSum += 1