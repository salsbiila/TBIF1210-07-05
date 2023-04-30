# Program menunjukkan serangkaian perintah menu yang dapat diakses dalam program
# I.S. Program berjalan
# F.S. Keluaran serangkaian menu yang bisa dipilih
# Membuat daftar command untuk tiap role 
# Pemain yang belum login
def help():
    print("===============================")
    print("   Selamat datang di helpdesk   ")
    print("===============================")
    akses = input("Masukkan role: ")
    print("===============================")

    if akses == "guest":
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

    elif akses == "Bandung Bondowoso" or akses == "bandung bondowoso":
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

    elif akses == "Roro Jonggrang" or akses == "roro jongrang":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. Ayam berkokok")
        print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")

    elif akses == "Jin Pengumpul" or akses == "jin pengumpul":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif akses == "Jin Pembangun" or akses == "jin pembangun":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    else:
        print("Akses tidak valid")















