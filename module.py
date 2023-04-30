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
    
    delimCount //= rowCount(file)-1
    listData = []

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
    print(listData)
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
        if dataList[i][1] == uname:
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

def makeStr(dataSum, dataList, columnNum):
    dataStr = ''
    for row in range(dataSum):
        for idx in range(columnNum):
            if idx != columnNum-1:
                dataStr += f'{dataList[row][idx]};'
            else:
                dataStr += f'{dataList[row][idx]}\n'
    
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
    for i in l:
        if int(i) > max:
            max = int(i)
        if int(i) < min:
            min = int(i)
    return (max,min)

def Bacafile(filename):
    f = open(filename,"r")
    return f

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

def leng(l):
    c = 0
    for i in l:
        c += 1
    return c

def ubah(l,x,y):
    k = ""
    for i in range(leng(l)):
        if l[i] != x:
            k += l[i]
        else:
            k += y
    return k

def pan(l,x):
    c = 1
    for i in l:
        if i == x:
            c += 1
    return c

def pisah(a,x):
    b = leng(a)
    d = pan(a,x)
    s = ["" for x in range(d)]
    c = 0
    k = 0
    while k < b :
        while a[k] != x and k < b - 1:
            s[c] += a[k]
            k += 1
        if k == b - 1:
            s[c] += a[k]
        k += 1
        c += 1
    return(s)

def bersih(l):
    k = ""
    i = 0
    while i < leng(l):
        if pan(l,l[i]) - 1 > 0:
            k += l[i]
            l = ubah(l,l[i],"")
        else:
            k += l[i]
            i += 1
    return k

def hapus(l,x):
    k = [0 for x in range(pan(l,x) - 1)]
    for i in range(leng(l)):
        True

def ppop(l):
    s = ""
    for i in range(leng(l) - 1):
        s += l[i]
    return s