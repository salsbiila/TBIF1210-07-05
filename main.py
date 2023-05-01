from module import *
from F01_LOGIN import *
from F02_LOGOUT import *
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
from F13_Load import *
from F14_SAVE import *
from F15_help import *
from F16 import *

folder = ""
Folder = Load(folder)

file = open(Folder + "/" + 'user.csv', 'r')
userData = file.read()
userDataList = makeList(userData, 3)
userDataSum = rowCount(userData)

file = open(Folder + "/" + 'candi.csv', 'r')
candiData = file.read()
candiDataList = makeList(candiData, 5)
candiDataSum = rowCount(candiData)

file = open(Folder + "/" + 'bahan_bangunan.csv', 'r')
bahanData = file.read()
bahanDataList = makeList(bahanData, 3)
bahanDataSum = rowCount(bahanData)

# belum final belum dibenerin
Urutanleksikal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
role = ''
namajin= '' 
playing = True
isLoggedIn = False

while playing:
    userInput = input('>>> ')

    if isLoggedIn == False:

        if userInput == 'login':    #F01
            role, namajin, isLoggedIn = login (userDataList, userDataSum,role, namajin, isLoggedIn)

        elif userInput == 'logout':
            logout(isLoggedIn)
    
        elif userInput == 'help': #F15
            help()

        elif userInput == 'exit':   #F16
            if exit():
                saveCandi(candiDataSum, candiDataList, userDataList, userDataSum, bahanDataList, bahanDataSum)
            playing = False

        else:
            print ("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    
    else:
        if userInput == 'logout':
            logout(isLoggedIn)
            isLoggedIn = False
    
        elif userInput == 'summonjin':    #F03
            userDataList = summonJin(userDataSum, userDataList, role)
            userDataSum += 1
            print(userDataList)
        
        elif userInput == 'hapusjin':   #F04
            userDataSum, userDataList, candiDataSum, candiDataList = hapusJin(userDataSum, userDataList, candiDataSum, candiDataList, role)
        
        elif userInput == 'ubahjin':    #F05
            userDataList = ubahJin(userDataSum, userDataList, role)
            print(userDataList)
        
        elif userInput == 'bangun': #F06
            if role != "jin_pembangun":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                candiDataList, candiDataSum, bahanDataList = bangun_candi (bahanDataList, candiDataList, candiDataSum, namajin)
                print(bahanDataList)
                print(candiDataList, candiDataSum)

        elif userInput == 'kumpul': #F07
            if role != "jin_pengumpul":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                bahanDataList = kumpul_candi (bahanDataList, bahanDataSum)
                bahanDataSum = 4
                print(bahanDataList)

        elif userInput == 'batchkumpul': #F08
            if role != "bandung_bondowoso":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                bahanDataList = kumpul (bahanDataList, bahanDataSum, userDataList, userDataSum)
                bahanDataSum = 4
                print(bahanDataList)

        elif userInput == 'batchbangun': #F08
            if role != "bandung_bondowoso":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                candiDataList, candiDataSum = bangun (bahanDataList, candiDataList, candiDataSum, userDataList, userDataSum)
                print(bahanDataList)
                print(candiDataList, candiDataSum)
        
        elif userInput == 'laporanjin': #F09
            if role != "bandung_bondowoso":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                laporanjin (candiDataList, bahanDataList, bahanDataSum, candiDataSum, userDataList, userDataSum, Urutanleksikal)
        
        elif userInput == 'laporancandi': #F10
            if role != "bandung_bondowoso":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                laporancandi (candiDataList, candiDataSum)

        elif userInput == 'hancurkancandi':
            if role != "bandung_bondowoso":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                hancurkancandi(candiDataList)
        
        elif userInput == 'ayamberkokok':
            if role != "rorojonggrang":
                print("Pemain tidak memiliki kemampuan ini")
            else:
                ayamberkokok(candiDataSum)
                playing = False
            
        elif userInput == 'help': #F15
            help()

        elif userInput == 'exit':   #F16
            if exit():
                saveCandi(candiDataSum, candiDataList, userDataList, userDataSum, bahanDataList, bahanDataSum)
            playing = False