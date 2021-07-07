def getSumOfSquares(upToNum):
    sumer = 0
    for i in range(upToNum+1):
        sumer = sumer + i**2
    return sumer

def getSquareOfSum(upToNum):
    sum = 0
    for i in range(upToNum+1):
        sum = sum + i
    return sum**2

def diffBetweenThem(uptoNum):
    return getSquareOfSum(uptoNum) - getSumOfSquares(uptoNum)

print(diffBetweenThem(100))