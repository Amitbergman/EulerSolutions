f = open("p081_matrix.txt", "r")

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

for i in range(lengthOfMatrix):
    best_overall[i][lengthOfMatrix-1] = mat[i][lengthOfMatrix-1]
    best_down[i][lengthOfMatrix-1] = mat[i][lengthOfMatrix-1]
    best_up[i][lengthOfMatrix-1] = mat[i][lengthOfMatrix-1]
    best_right[i][lengthOfMatrix-1] = mat[i][lengthOfMatrix-1]

for ind in range(1, lengthOfMatrix):
    currentCol = lengthOfMatrix-1-ind
    #Calculate the best if we must go right
    for i in range(lengthOfMatrix):
        best_right[i][currentCol] = best_overall[i][currentCol+1] + mat[i][currentCol]

    #calculate the best if we can go right or up
    for i in range(lengthOfMatrix):
        if(i==0):
            best_up[0][currentCol] = best_right[0][currentCol]
        else:
            best_up[i][currentCol] = mat[i][currentCol] + min(best_overall[i][currentCol+1], best_up[i-1][currentCol])
    
    #calculate the best if we can go right or down
    for i in range(lengthOfMatrix):
        index = lengthOfMatrix-i-1
        if(index ==lengthOfMatrix - 1):
            best_down[index][currentCol] = best_right[index][currentCol]
        else:
            best_down[index][currentCol] = mat[index][currentCol] + min(best_overall[index][currentCol+1], best_down[index+1][currentCol])

    for i in range(lengthOfMatrix):
        best_overall[i][currentCol] = min(best_down[i][currentCol], best_up[i][currentCol])




def getBestByIndexes(col, row):
    if (col == lengthOfMatrix - 1):
        return mat[col][row]
    if (col ==lengthOfMatrix - 1):
        return mat[col][row] + best_overall[col][row+1]
    if (row == lengthOfMatrix - 1):
        return mat[col][row] + best_overall[col+1][row]
    return mat[col][row] + min(best_overall[col+1][row], best_overall[col][row+1])

overAllBest = min([a[0] for a in best_overall])
print("The solution to euler 82 is:", overAllBest)