import argparse
import os

def Load(folder):
    parser = argparse.ArgumentParser(description='Memproses Folder')
    parser.add_argument('nama_folder', type=str, nargs = '?', help='Input nama folder yang akan di Load')
    args = parser.parse_args()
    folder = args.nama_folder

    if folder == None:
        print("Tidak ada nama folder!\nContoh penulisan yang benar: python main.py <nama_folder>")
        exit()
    elif os.path.isdir(folder):
        print("Loading...")
        print("Selamat datang di game Candi, Roro, Jin dan Bondowoso")
        print("Silahkan login terlebih dahulu")
    else:
        print("\nFolder", folder, "tidak ditemukan")
        exit()
    return folder
