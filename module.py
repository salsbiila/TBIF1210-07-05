file = open('user.csv', 'r')
userData = file.read()
file = open('candi.csv', 'r')
candiData = file.read()
file = open('bahan_bangunan.csv', 'r')
bahanData = file.read()

def rowCount(file):
    count = 1
    for letter in file:
        if letter == '\n':
            count += 1
    return count

def makeList(file, delim = ';'):
    delimCount = 0
    for letter in file:
        if letter == delim:
            delimCount += 1
    
    delimCount //= rowCount(file)
    if delimCount == 2:
        listData = [['', '', ''] for i in range (rowCount(file))]
    elif delimCount == 4:
        listData = [['', '', '', '', ''] for i in range (rowCount(file))]
    row = 0
    idx = 0 # kolom
    data = ''
    currentLength = 1
    for letter in file:
        if letter == delim:
            listData[row][idx] = data
            data = ''
            idx += 1
        elif letter == '\n':
            listData[row][idx] = data
            data = ''
            row += 1
            idx = 0
        elif currentLength == len(file):
            data += letter
            listData[row][idx] = data
        else:
            data += letter
        currentLength += 1
    return listData

def updateUserDataList(uname, password, jinRole, list, file = userData):
    newListData = [['', '', ''] for i in range (rowCount(file)+1)]
    for row in range(rowCount(file)):
        for idx in range(3):    #idx adalah kolom
            newListData[row][idx] = list[row][idx]
    newListData[rowCount(file)][0] = uname
    newListData[rowCount(file)][1] = password
    newListData[rowCount(file)][2] = jinRole

    return newListData

def updateUserData(uname, password, jinRole, file = userData):
    file += f'\n{uname};{password};{jinRole}'

    return file

def updateCandiDataList(id, pembuat, pasir, batu, air, list, file = candiData):
    newListData = [['', '', ''] for i in range (rowCount(file)+1)]
    for row in range(rowCount(file)):
        for idx in range(5):    #idx adalah kolom
            newListData[row][idx] = list[row][idx]
    newListData[rowCount(file)][0] = id
    newListData[rowCount(file)][1] = pembuat
    newListData[rowCount(file)][2] = pasir
    newListData[rowCount(file)][3] = batu
    newListData[rowCount(file)][4] = air

    return newListData

def updateCandiData(id, pembuat, pasir, batu, air, file = candiData):
    file += f'\n{id};{pembuat};{pasir};{batu};{air}'

    return file

def updateBahanDataList(nama, deskripsi, jumlah, list, file = bahanData):
    newListData = [['', '', ''] for i in range (rowCount(file)+1)]
    for row in range(rowCount(file)):
        for idx in range(3):    #idx adalah kolom
            newListData[row][idx] = list[row][idx]
    newListData[rowCount(file)][0] = nama
    newListData[rowCount(file)][1] = deskripsi
    newListData[rowCount(file)][2] = jumlah

    return newListData

def updateBahanData(nama, deskripsi, jumlah, file = bahanData):
    file += f'\n{nama};{deskripsi};{jumlah}'

    return file