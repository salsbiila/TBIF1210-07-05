def exit():
    userInput = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while userInput != 'y' and userInput != 'n':
        userInput = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if userInput == "y":
        return True