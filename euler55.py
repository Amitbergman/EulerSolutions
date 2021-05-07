def isPelindrome(num):
    numAsStr = str(num)
    length = len(numAsStr)
    for i in range(int(length / 2)):
        if (numAsStr[i] != numAsStr[length - 1-i]):
            return False
    return True

def reversedNumber(num):
    return int(str(num)[::-1])

def plusReversed(num):
    return num + reversedNumber(num)

def checkLychrel(num):
    tocheck = num
    for i in range(60):
        tocheck = plusReversed(tocheck)
        if (isPelindrome(tocheck)):
            return False #found a palindrome, it is not Lychrel number
    return True

counter = 0
for i in range(10000):
    if (checkLychrel(i)):
        counter +=1
print(counter)