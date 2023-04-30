import os
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
    candiFile.write ("id;pembuat;pasir;batu;air\n") #menulis file 
    for i in range (candiNeff):
        if candiList [i] != ("", "", "", "", ""):
            string = str (candiList[i][0] + ";" + candiList[i][1]+ ";" + str (candiList [1][2]) + ";" + str (candiList[1][3]) + ";" + str (candiList[1][4]))
            candiFile.write (string + '\n')
    bahanBangunanFile = open ("bahan_bangunan.csv", 'w') #digunakan untuk membuka file bahan bangunan
    bahanBangunanFile.write ("nama;deskripsi;jumlah\n") #menulis file
    for i in range (lenBahanList):
        if bahanList != ("", "", ""):
            string = bahanList [i][0] + ';' + bahanList [i][1] + ';' + str (bahanList [i][2])
            bahanBangunanFile.write(string+"\n")
    userFile = open ("user.csv", 'w') #digunakan untuk membuka file user 
    userFile.write ("username;password;role\n") #menulis file
    for i in range (userNeff):
        if userList [i] != ("", "", ""):
            string = userList [i][0] + ';' + userList [i][1] + ';' + userList[i][2]
            userFile.write (string + "\n")
    userFile.close() #digunakan untuk menutup file user
    candiFile.close() #untuk menutup file candi
    bahanBangunanFile.close() #untuk menutup file bahan bangunan
    print ("Berhasil menyimpan data di folder ", os.getcwd())