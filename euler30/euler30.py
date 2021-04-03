import time
import threading

theSumOfAll = 0
GeneralStartTime = time.time()


d = dict()
d[1] = 1
d[0] = 0
d[2] = 2**5
d[3] = 3**5
d[4] = 4**5
d[5] = 5**5
d[6] = 6**5
d[7] = 7**5
d[8] = 8**5
d[9] = 9**5

def sumOfPower(number):
    sumer = 0
    while(number > 0):
        sumer += d[number%10]
        number = number // 10
    return sumer

#the largest number that you can get with 5 digits is of 6 digits
# the smallest number that you can get with 5 digits is of 1 digit

#the largest number that you can get with 6 digits is of 6 digits
# the smallest number that you can get with 6 digits is of 1 digit

#the largest number that you can get with 7 digits is of 6 digits, so there is no point to check 7 digits numbers
#Actually the largest number that you should check is 354294 = 9**5 * 6

numberOfThreads = 4
end = 354294
start = 2

rangeForEach = (end - start) // numberOfThreads

def workForThread(start, threadName):
    global theSumOfAll
    startTime = time.time()
    for i in range (2,354294, 4):
        if (sumOfPower(i) == i):
            theSumOfAll += i
    endTime = time.time()
    print(endTime - startTime, "is the time it took thread ", threadName)

threads = list()
for index in range(numberOfThreads):
    x = threading.Thread(target=workForThread, args=(2+index, index))
    threads.append(x)
    x.start()
for index, thread in enumerate(threads):
    thread.join()

print(theSumOfAll)
GeneralEndTime = time.time()
print("shoule be 443839")
print("generally it took", GeneralEndTime - GeneralStartTime)