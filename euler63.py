def solveForN(n):
    
    current = 1
    counterForCurrent = 0
    while (True):
        toCheck = current **n
        length = len(str(toCheck))
        if(length == n):
            counterForCurrent +=1
        if (length > n ):
            break
        current+=1
    return counterForCurrent
counter = 0

for i in range(22): #No need to check more than 22, since len(str(9**22)) = 21 and len(str(10**22)) = 23 so after 10 it is too much and before too little numbers
    counter += solveForN(i)
print(counter)