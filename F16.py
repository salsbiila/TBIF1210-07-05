def exitProcedure():
    ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if ans == "y":
        return True
    elif ans == "n":
        return False