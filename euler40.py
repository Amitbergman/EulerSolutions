index = 0
mult = 1
detected = 0
i=1
lookingFor = 1

import time
tic = time.perf_counter()
while(detected < 7):
    cur = str(i)
    a = len(cur)
    if (a + index < lookingFor):
        index += a
    else:
        desiredLetter = cur[lookingFor - index-1]
        lookingFor = lookingFor * 10
        detected = detected + 1
        mult = mult * int(desiredLetter)
        index += a
    i = i + 1
after = time.perf_counter()
print(after - tic)
print(mult)

#0.15897660000000002


    
