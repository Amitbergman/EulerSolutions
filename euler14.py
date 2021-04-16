a = dict()
a[1] = 1

def calculateCollatzSequenceLength(num):
    if (int(num) in a):
        return a[int(num)]
    if (num%2 ==0):
        return 1 + calculateCollatzSequenceLength(num/2)
    return 1 + calculateCollatzSequenceLength(3 * num + 1)

maxer = 0
indOfMax = 0
for i in range(2,1000000):
    col_length = calculateCollatzSequenceLength(i)
    a[i] = col_length
    if (col_length > maxer):
        indOfMax = i
        maxer = col_length

print(str(indOfMax) + " with length of " +  str(maxer) + " is the winner")