f = open("numbers.txt", "r")
a = f.readlines()

numbers = [[0 for k in range(20)] for i in range(20)]

for i in range(20):
    line = a[i].split()
    for j in range(20):
        numbers[i][j] = int(line[j])

def calcDiag(arr, i,j):
    try:
        res = 1
        for k in range(4):
            res = res * arr[i+k][j+k]
        return res
    except:
        return 0

def calcCounterDiag(arr, i,j):
    try:
        res = 1
        for k in range(4):
            res = res * arr[i+k][j-k]
        return res
    except:
        return 0

def calcDown1(arr,i,j):
    try:
        res = 1
        for k in range(4):
            res = res * arr[i+k][j]
        return res
    except:
        return 0

def calcRight(arr,i,j):
    try:
        res = 1
        for k in range(4):
            res = res * arr[i][j+k]
        return res
    except:
        return 0

maxer = 0
row = 0
column = 0
resOface = 0
for i in range (20):
    for j in range (20):
        diag = calcCounterDiag(numbers, i, j)
        down = calcDown1(numbers, i, j)
        right = calcRight(numbers, i, j)
        curMax = max(max(right, down), diag)
        if (curMax > maxer):
            maxer = curMax
            row = i
            column = j
            resOface = numbers[i][j]

print(maxer)        
print(row)        
print(column)        
print(resOface)        