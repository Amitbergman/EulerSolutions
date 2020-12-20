
#a**2 + b**3 + c**4 = k
# k < 50,000,000
import math, time
tic = time.perf_counter()

fiftyMiliion = 50000000
sqrtFiftyMillion = math.sqrt(fiftyMiliion)
primes_up_to_sqrt_fifty_million = [True for i in range(int(sqrtFiftyMillion+1))]
primes_up_to_sqrt_fifty_million[0] = False
primes_up_to_sqrt_fifty_million[1] = False

for i in range(2,int(sqrtFiftyMillion)):
    cur = i*i
    while (cur < sqrtFiftyMillion):
        primes_up_to_sqrt_fifty_million[cur] = False
        cur = cur + i

optionsForA = []
optionsForB = []
optionsForC = []

for i in range(int(sqrtFiftyMillion)+1):
    if (primes_up_to_sqrt_fifty_million[i] == False):
        continue
    if (i**4 < fiftyMiliion):
        optionsForC.append(i)
    if (i**3 < fiftyMiliion):
        optionsForB.append(i)
    optionsForA.append(i)


# These are all the options to get a,b,c so that:
allTheResults = set()
a=0
b=0

for c in optionsForC:
    for b in optionsForB:
        if (c**4 + b**3 >= fiftyMiliion):
            break
        for a in optionsForA:
            cur = a**2 + b**3 + c**4
            if (cur >= fiftyMiliion):
                break
            else:
                allTheResults.add(cur)
after = time.perf_counter()

print("Result is: " + str(len(allTheResults)))
print("It took " + str(after - tic) + " seconds")
