def isIncreasing(num):
    currentNumber = num %10
    whole = num // 10
    while (whole > 0):
        if (currentNumber >= whole %10):
            currentNumber = int(whole %10)
            whole = int(whole / 10)
        else:
            return False
    return True

def isDecreasing(num):
    currentNumber = num %10
    whole = num //10
    while (whole > 0):
        if (currentNumber <= whole %10):
            currentNumber = int(whole %10)
            whole = int(whole / 10)
        else:
            return False
    return True

def isBouncy(num):
    return not(isDecreasing(num)) and not(isIncreasing(num))

def percentageBelow(end):
    counter = 0
    for i in range(end+1):
        if (isBouncy(i)):
            counter+=1
    print(counter)
    return counter / end

percentage = 0
general = 0
bouncy = 0
toCheck = 1
goal = 0.99
while (percentage < goal):
    if (isBouncy(toCheck)):
        bouncy +=1
    toCheck +=1
    general +=1
    percentage = bouncy / general

print("Answer to euler 112 is: ", general)
