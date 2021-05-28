f = open("p081_matrix.txt", "r")
import random
line = f.readline()
lengthOfMatrix = len(line.split(','))

mat = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]
best_up = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]
best_down = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]
best_right = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]
best_overall = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]

#Read the data
for i in range(lengthOfMatrix):
    mat[i] = [int(k) for k in line.split(',') ]
    line = f.readline()
    
f.close()

visited = [(0,0)]

def isLegal(row, col):
    return col >=0 and row >=0 and col <= lengthOfMatrix-1 and row <= lengthOfMatrix -1

def visitedInIt(row, col):
    return visited.count((row, col)) >0

def getNext(row, col, greedy=False):
    options = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)] + [(row+1, col), (row, col+1)]*2
    legal_options = [(i,mat[i[0]][i[1]]) for i in options if (isLegal(i[0], i[1]) and not(visitedInIt(i[0], i[1])))]
    for a in legal_options:
        visited.append(a)
    if (len(legal_options) ==0):
        return (-1,-1)
    res = random.choice(legal_options)[0]
    if (greedy):
        res = min(legal_options, key = lambda a: a[1])[0]
    return res

best_overall[lengthOfMatrix-1][lengthOfMatrix-1] = mat[lengthOfMatrix-1][lengthOfMatrix-1]

minSum = 800000
while True:
    currentSum = 0
    currentRow = 0
    currentCol = 0
    visited = [(currentRow,currentCol)]
    failure = False
    counter = 0
    while (not(currentRow == lengthOfMatrix -1 and currentCol == lengthOfMatrix-1)):
        currentSum = currentSum + mat[currentRow][currentCol]
        (currentRow, currentCol) = getNext(currentRow, currentCol, greedy=True)
        if (currentCol < 0 or currentSum > minSum):
            failure = True
            break
        counter = counter + 1
    currentSum = currentSum + mat[currentRow][currentCol]     
    if (currentSum < minSum and not(failure)):
        minSum = currentSum
        print("the sum is:", currentSum)