from module import *
from F01_LOGIN import *
from F03 import *
from F04 import *
from F05 import *
from F06_jin_pembangun import *
from F07_Jin_pengumpul import *
from F08_KumpulBangun import *
from f09 import *
from f10 import *
from f11 import *
from f12 import *
from F14_SAVE import *
from F15_help import *
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
Urutanleksikal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
role = ''
namajin= '' 
playing = True

while playing:
    userInput = input('>>> ')

    if userInput == 'login':    #F01
        role, namajin = login (userDataList, userDataSum,role, namajin)
    
    elif userInput == 'summonjin':    #F03
        userDataList = summonJin(userDataSum, userDataList)
        userDataSum += 1
        print(userDataList)
    
    elif userInput == 'hapusjin':   #F04
        userDataSum, userDataList, candiDataSum, candiDataList = hapusJin(userDataSum, userDataList, candiDataSum, candiDataList)
    
    elif userInput == 'ubahjin':    #F05
        userDataList = ubahJin(userDataSum, userDataList)
        print(userDataList)
    
    elif userInput == 'bangun': #F06
        if role != "jin_pembangun":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            candiDataList, candiDataSum = bangun_candi (bahanDataList, candiDataList, candiDataSum, namajin)
            print(bahanDataList)
            print(candiDataList, candiDataSum)

    elif userInput == 'kumpul': #F07
        if role != "jin_pengumpul":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            kumpul_candi (bahanDataList)
            print(bahanDataList)

    elif userInput == 'batchkumpul': #F08
        if role != "bondowoso":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            kumpul (bahanDataList, userDataList, userDataSum)
            print(bahanDataList)

    elif userInput == 'batchbangun': #F08
        if role != "bondowoso":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            candiDataList, candiDataSum = bangun (bahanDataList, candiDataList, candiDataSum, userDataList, userDataSum)
            print(bahanDataList)
            print(candiDataList, candiDataSum)
    
    elif userInput == 'laporanjin': #F09
        if role != "bondowoso":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            laporanjin (candiDataList, bahanDataList, candiDataSum, userDataList, userDataSum, Urutanleksikal)
    
    elif userInput == 'laporancandi': #F10
        if role != "bondowoso":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            laporancandi (candiDataList, candiDataSum)

    elif userInput == 'hancurkancandi':
        if role != "bondowoso":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            hancurkancandi(candiDataList)
    
    elif userInput == 'ayamberkokok':
        if role != "rorojonggrang":
            print("Pemain tidak memiliki kemampuan ini")
        else:
            ayamberkokok(candiDataSum)

    elif userInput == 'help': #F15
        help()

    elif userInput == 'exit':   #F16
        if exit():
            saveCandi(candiDataSum, candiDataList, userDataList, userDataSum, bahanDataList, bahanDataSum)
        playing = False
