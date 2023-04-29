def logout ():
    global is_login, role
    if is_login:
        print ("Logout berhasil")
        role = None
        is_login = False 
    else:
        print ("Logout gagal!")
        print ("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

logout ()