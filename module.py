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

def updateDataList3(param1, param2, param3, list, file = userData):
    newListData = [['', '', ''] for i in range (rowCount(file)+1)]
    for row in range(rowCount(file)):
        for idx in range(3):    #idx adalah kolom
            newListData[row][idx] = list[row][idx]
    newListData[rowCount(file)][0] = param1
    newListData[rowCount(file)][1] = param2
    newListData[rowCount(file)][2] = param3

    return newListData

def updateData3(param1, param2, param3, file = userData):
    file += f'\n{param1};{param2};{param3}'

    return file

def updateDataList5(param1, param2, param3, param4, param5, list, file = candiData):
    newListData = [['', '', ''] for i in range (rowCount(file)+1)]
    for row in range(rowCount(file)):
        for idx in range(5):    #idx adalah kolom
            newListData[row][idx] = list[row][idx]
    newListData[rowCount(file)][0] = param1
    newListData[rowCount(file)][1] = param2
    newListData[rowCount(file)][2] = param3
    newListData[rowCount(file)][3] = param4
    newListData[rowCount(file)][4] = param5

    return newListData

def updateData5(param1, param2, param3, param4, param5, file = candiData):
    file += f'\n{param1};{param2};{param3};{param4};{param5}'

    return file

def deleteUser(uname, list, file = userData):
    deletionCount = 0
    for i in range(1, rowCount(file)):
        if list[i][0] == uname:
            list[i] = None
            deletionCount += 1
    
    newListData = [['', '', ''] for i in range (rowCount(file)-deletionCount)]
    
    row = 0
    for i in range(rowCount(file)):
        if list[i] != None:
            newListData[row] = list[i]
            row += 1
    
    return newListData #belum selesai