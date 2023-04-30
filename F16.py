def exit():
    userInput = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")

    while userInput != 'Y' and userInput != 'N':
        userInput = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")

    if userInput == "Y":
        return True