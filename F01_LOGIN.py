user = [["","",""] for i in range (102)]
user[0]=['Bondowoso', 'cintaroro', 'bandung_bondowoso']
user[1]=['Roro', 'gasukabondo', 'roro_jonggrang']

is_login = False
def login (user):
    global is_login, role
    if not is_login:
        username = input ("Username : ")
        password = input ("Password : ")
        validUsername = False
    
        for i in range (102):
            if username == user [i][0]:
                validUsername = True
                if password == user [i][1]:
                    role = user [i][2]
                    print ("Selamat datang, " + username + "!")
                    print ('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                    is_login = True 
                    break
                else :
                    print ("Password salah !")
        if not validUsername:
            print ("Username salah!")
    else :
        print ("Login gagal !")
        print ("Anda telah login dengan username" + username + ', , silakan lakukan "logout" sebelum melakukan login kembali.')
login (user)