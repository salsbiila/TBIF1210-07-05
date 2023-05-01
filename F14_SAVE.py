import os
from module import *
#importing os module

def saveCandi (candiNeff, candiList, userList, userNeff, bahanList, lenBahanList):
    namaFolder = input ("Masukkan nama folder : ")
    print ("\n Saving... \n")
    if not os.path.exists(namaFolder): #untuk memeriksa apakah suatu file ada atau tidak ada 
        os.mkdir(namaFolder) #digunakan untuk membuat direktori bernama namaFolder
        os.chdir(namaFolder) #untuk mengubah direktori
        print ("Membuat folder", os.getcwd()) #untuk mendapatkan direktori tempat file yang sedang dilakukan
        print ()
    else:
        os.chdir (namaFolder)
    candiFile = open ("candi.csv", 'w') #digunakan untuk membuka file candi
    candiNeff, candiList = deleteCandi('', candiNeff, candiList)
    candiFile.write(makeStr(candiNeff, candiList, 5))
    
    bahanBangunanFile = open ("bahan_bangunan.csv", 'w') #digunakan untuk membuka file bahan bangunan
    lenBahanList, bahanList = deleteUser('', lenBahanList, bahanList)
    bahanBangunanFile.write(makeStr(lenBahanList, bahanList, 3))
    
    userFile = open ("user.csv", 'w') #digunakan untuk membuka file user 
    userFile.write(makeStr(userNeff, userList, 3, False))
    
    userFile.close() #digunakan untuk menutup file user
    candiFile.close() #untuk menutup file candi
    bahanBangunanFile.close() #untuk menutup file bahan bangunan
    print ("Berhasil menyimpan data di folder ", os.getcwd())