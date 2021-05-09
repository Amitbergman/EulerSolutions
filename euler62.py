setOfCubes = set()
for i in range(10000):
    setOfCubes.add(i**3)
print("Done step 1")
def isPermutation(a,b):
    if (len(a) != len(b)):
        return False
    d = dict()
    for i in a:
        if (i in d):
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in b:
        if (i in d and d[i] > 0):
            d[i] = d[i] - 1
        else:
            return False
    return True
    
print("Done step 2")

dictionartOfPerms = dict()
index = 0
for i in setOfCubes:
    if (index %1000 ==0):
        print(index)
    index +=1
    for j in setOfCubes:
        if isPermutation(str(i), str(j)):
            if (i in dictionartOfPerms):
                dictionartOfPerms[i].append(j)
            else:
                if (j in dictionartOfPerms):
                    dictionartOfPerms[j].append(i)
                else:
                    dictionartOfPerms[i] = [i,j]
print("Done step 3")

inFivers = []
for i in dictionartOfPerms:
    dictionartOfPerms[i] = list(set(dictionartOfPerms[i]))
    if (len(dictionartOfPerms[i]) == 5):
        inFivers.append(min(dictionartOfPerms[i]))
        print(dictionartOfPerms[i])


print("the answer is:", min(inFivers))

            
