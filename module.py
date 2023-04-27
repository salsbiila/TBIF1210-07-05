def rowCount(file): # hanya untuk di awal
    count = 1
    for letter in file:
        if letter == '\n':
            count += 1
    return count

def makeList(file, delim = ';'): # hanya untuk membuat list pertama
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

def updateDataList3(param1, param2, param3, dataSum, dataList):
    newListData = [['', '', ''] for i in range (dataSum+1)]
    for row in range(dataSum):
        for idx in range(3):    #idx adalah kolom
            newListData[row][idx] = dataList[row][idx]
    newListData[dataSum][0] = param1
    newListData[dataSum][1] = param2
    newListData[dataSum][2] = param3

    return newListData

def updateDataList5(param1, param2, param3, param4, param5, dataSum, dataList):
    newListData = [['', '', ''] for i in range (dataSum+1)]
    for row in range(dataSum):
        for idx in range(5):    #idx adalah kolom
            newListData[row][idx] = dataList[row][idx]
    newListData[dataSum][0] = param1
    newListData[dataSum][1] = param2
    newListData[dataSum][2] = param3
    newListData[dataSum][3] = param4
    newListData[dataSum][4] = param5

    return newListData

def deleteUser(uname, dataSum, dataList):
    # Deleting di list
    deletionCount = 0
    for i in range(1, dataSum):
        if dataList[i][0] == uname:
            dataList[i] = None
            deletionCount += 1
    
    newListData = [['', '', ''] for i in range (dataSum-deletionCount)]
    
    row = 0
    for i in range(dataSum):
        if list[i] != None:
            newListData[row] = list[i]
            row += 1
    
    return newListData

def makeStr(sum, dataList, columnNum):
    dataStr = ''
    for row in range(sum):
        for idx in range(columnNum):
            if idx != columnNum-1:
                dataStr += f'{dataList[row][idx]};'
            else:
                dataStr += f'{dataList[row][idx]}\n'
    
    return dataStr