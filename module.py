def rowCount(file): # hanya untuk di awal
    count = 1
    for letter in file:
        if letter == '\n':
            count += 1

    return count

def makeList(file, x, delim = ';'): # hanya untuk membuat list pertama
    if x == 3:
        listData = [['', '', ''] for i in range (rowCount(file))]
    elif x == 5:
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
    newListData = [['', '', '', '', ''] for i in range (dataSum+1)]
    for row in range(dataSum):
        for idx in range(5):    #idx adalah kolom
            newListData[row][idx] = dataList[row][idx]
    newListData[dataSum-1][0] = param1
    newListData[dataSum-1][1] = param2
    newListData[dataSum-1][2] = param3
    newListData[dataSum-1][3] = param4
    newListData[dataSum-1][4] = param5

    return newListData

def deleteUser(uname, dataSum, dataList):
    deletionCount = 0
    for i in range(1, dataSum):
        if dataList[i][0] == uname:
            dataList[i] = None
            deletionCount += 1
    
    newListData = [['', '', ''] for i in range (dataSum-deletionCount)]
    
    row = 0
    for i in range(dataSum):
        if dataList[i] != None:
            newListData[row] = dataList[i]
            row += 1
    
    newSum = dataSum - deletionCount
    return newSum, newListData

def deleteCandi(uname, dataSum, dataList):
    deletionCount = 0
    for i in range(1, dataSum):
        if dataList[i][0] == uname:
            dataList[i] = None
            deletionCount += 1
    
    newListData = [['', '', '', '', ''] for i in range (dataSum-deletionCount)]
    
    row = 0
    for i in range(dataSum):
        if dataList[i] != None:
            newListData[row] = dataList[i]
            row += 1
    
    newSum = dataSum - deletionCount
    return newSum, newListData

def makeStr(dataSum, dataList, columnNum, addEnter = True):
    dataStr = ''
    for row in range(dataSum):
        for idx in range(columnNum):
            if row != dataSum - 1:
                if idx != columnNum-1:
                    dataStr += f'{dataList[row][idx]};'
                else:
                    dataStr += f'{dataList[row][idx]}\n'
            else:
                if idx != columnNum-1:
                    dataStr += f'{dataList[row][idx]};'
                else:
                    if addEnter:
                        dataStr += f'{dataList[row][idx]}\n'
                    else:
                        dataStr += f'{dataList[row][idx]}'

    
    return dataStr

def switchRole(row, dataSum, dataList):
    newDataList = [['', '', ''] for i in range (dataSum)]

    for i in range(dataSum):
        for j in range(3):
            if i == row and j == 2:
                if dataList[i][j] == 'jin_pengumpul':
                    newDataList[i][j] = 'jin_pembangun'
                elif dataList[i][j] == 'jin_pembangun':
                    newDataList[i][j] = 'jin_pengumpul'
            else:
                newDataList[i][j] = dataList[i][j]
    
    return newDataList

def maxmin(l):
    max = int(l[0])
    min = int(l[0])
    for i in range(leng(l)):
        if int(l[i]) > max:
            max = int(l[i])
        if int(l[i]) < min:
            min = int(l[i])
    return (max,min)

def leng(l):
    c = 0
    X = 0
    for i in range(100):
        X += 1
        temp = [None for i in range (X)]
        for k in range (X):
            temp[k] = l[k]
        c += 1
        if temp == l:
            break
    return c

def uang(l):
    c = leng(l) - 1
    hasil = ""
    for i in range(leng(l)):
        if c % 3 == 0 and i != (leng(l) - 1):
            hasil += l[i] + "."
        else:
            hasil += l[i]
        c -= 1
    return hasil

def pan(l,x):
    c = 1
    for i in range(leng(l)):
        if l[i] == x:
            c += 1
    return c

def cariIdx(l,x):
    for i in range(leng(l)):
        if l[i] == x:
            index = i
    return index