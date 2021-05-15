lengthOfMatrix = 80
f = open("p081_matrix.txt", "r")
mat = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]
best = [[0 for i in range(lengthOfMatrix)] for i in range(lengthOfMatrix)]

#Read the data
for i in range(lengthOfMatrix):
    line = f.readline()
    mat[i] = [int(k) for k in line.split(',') ]

f.close()

def getBestByIndexes(col, row):
    if (col == row == lengthOfMatrix - 1):
        return mat[col][row]
    if (col ==lengthOfMatrix - 1):
        return mat[col][row] + best[col][row+1]
    if (row == lengthOfMatrix - 1):
        return mat[col][row] + best[col+1][row]
    return mat[col][row] + min(best[col+1][row], best[col][row+1])

for i in range(lengthOfMatrix):
    for j in range(lengthOfMatrix):
        #go over the solutions from the end to the start
        column = lengthOfMatrix-i-1
        row = lengthOfMatrix-j-1
        best[column][row] = getBestByIndexes(column, row)

print("The solution to euler 81 is:", best[0][0])