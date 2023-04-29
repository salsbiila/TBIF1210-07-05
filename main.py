from module import *
from F03 import *
from F04 import *
from F05 import *
from F06_jin_pembangun import *
from F07_Jin_pengumpul import *
from F08_KumpulBangun import *
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
        print(userDataList)
    
    elif userInput == 'hapusjin':   #F04
        userDataSum, userDataList, candiDataSum, candiDataList = hapusJin(userDataSum, userDataList, candiDataSum, candiDataList)
    
    elif userInput == 'ubahjin':    #F05
        userDataList = ubahJin(userDataSum, userDataList)
        print(userDataList)
    
    elif userInput == 'bangun': #F06
        candiDataList, candiDataSum = bangun_candi (bahanDataList, candiDataList, candiDataSum)
        print(bahanDataList)
        print(candiDataList, candiDataSum)

    elif userInput == 'kumpul': #F07
        kumpul_candi (bahanDataList)
        print(bahanDataList)

    elif userInput == 'batchkumpul': #F08
        kumpul (bahanDataList, userDataList, userDataSum)
        print(bahanDataList)

    elif userInput == 'batchbangun': #F08
        candiDataList, candiDataSum = bangun (bahanDataList, candiDataList, candiDataSum, userDataList, userDataSum)
        print(bahanDataList)
        print(candiDataList, candiDataSum)

    elif userInput == 'exit':   #F16
        if exit():
            print('masuk ke f14')
        playing = False
