index = 0
mult = 1
detected = 0
i=1
lookingFor = 1

import time
tic = time.perf_counter()
while(detected < 7):
    cur = str(i)
    i = i + 1
    currentNumberLength = len(cur)
    if (currentNumberLength + index >= lookingFor):
        desiredLetter = cur[lookingFor - index-1]
        lookingFor = lookingFor * 10
        detected = detected + 1
        mult = mult * int(desiredLetter)
    index += currentNumberLength
after = time.perf_counter()
print("it took " + str(after - tic) + " seconds")
print("result is: " + str(mult))



    
