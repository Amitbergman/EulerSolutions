

d = dict()
d['1'] = 1
d['0'] = 0
d['2'] = 2**5
d['3'] = 3**5
d['4'] = 4**5
d['5'] = 5**5
d['6'] = 6**5
d['7'] = 7**5
d['8'] = 8**5
d['9'] = 9**5

def sumOfPower(number):
    sumer = 0
    for i in number:
        sumer += d[i]
    return sumer

#the largest number that you can get with 5 digits is of 6 digits
# the smallest number that you can get with 5 digits is of 1 digit

#the largest number that you can get with 6 digits is of 6 digits
# the smallest number that you can get with 6 digits is of 1 digit

#the largest number that you can get with 7 digits is of 6 digits, so there is no point to check 7 digits numbers
#Actually the largest number that you should check is 354294 = 9**5 * 6
theSumOfAll = 0
for i in range (2,354296):
    numAsString = str(i)
    theSum = sumOfPower(numAsString)
    if ((theSum) == i):
        theSumOfAll += i

print(theSumOfAll)
