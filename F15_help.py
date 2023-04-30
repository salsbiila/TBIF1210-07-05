# Program menunjukkan serangkaian perintah menu yang dapat diakses dalam program
# I.S. Program berjalan
# F.S. Keluaran serangkaian menu yang bisa dipilih
# Membuat daftar command untuk tiap role 
# Pemain yang belum login
def belum_login():
    print("=========== HELP ===========")
    print("1. login")
    print("   Untuk masuk menggunakan akun")
    print("2. exit")
    print("   Untuk keluar dari program dan kembali ke terminal")
# Bandung bondowoso
def bandung_bondowoso ():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. summonjin")
    print("   Untuk memanggil jin")
    print("3. hapusjin")
    print("   Untuk menghapus jin yang dipanggil")
    print("4. ubahjin")
    print("   Untuk mengubah atribut jin yang dipanggil")
    print("5. batchkumpul")
    print("   Untuk mengumpulkan resource candi secara berulang")
    print("6. batchbangun")
    print("   Untuk membangun candi secara berulang")
    print("7. laporanjin")
    print("   Untuk menampilkan laporan mengenai jin yang dipanggil")
    print("8. laporancandi")
    print("   Untuk menampilkan laporan mengenai candi yang telah dibangun")
# Roro Jongrang
def roro_jongrang():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. hancurkancandi")
    print("   Untuk menghancurkan candi yang tersedia")
    print("3. Ayam berkokok")
    print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari  ")
# Jin Pengumpul
def jin_pengumpul():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. kumpul")
    print("   Untuk mengumpulkan resource candi")
# Jin Pembangun
def jin_pembangun():
    print("=========== HELP ===========")
    print("1. logout")
    print("   Untuk keluar dari akun yang digunakan sekarang")
    print("2. bangun")
    print("   Untuk membangun candi")
# Akses
print ('==============================')
print ('  Selamat datang di helpdesk  ')
print ('==============================')
akses = input(" masukkan role: ")
if akses == "guest" : #belum login
    belum_login()
elif akses == "Bandung Bondowoso" or akses == "bandung bondowoso":
    bandung_bondowoso()
elif akses == "Roro Jonggrang" or akses == "roro jongrang":
    roro_jongrang()
elif akses == "Jin Pengumpul" or akses == "jin pengumpul":
    jin_pengumpul()
elif akses == "Jin Pembangun" or akses == "jin pembangun":
    jin_pembangun()
else:
    print("Akses tidak valid")















