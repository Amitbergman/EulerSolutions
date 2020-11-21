def greater(l,i,j):
    return l[i][0] > l[j][0] and l[i][1] > l[j][1]

f = open("C:\\Users\\ambergma\\Desktop\\Amit\\Project euler\\euler_99\\p099_base_exp.txt", "r")
import time
import math
t0 = time.perf_counter()

l_1 = list()
l_2 = list()
a = 0
for x in f:
    splitted = x.split(",")
    l_1.append((int(splitted[0]), int(splitted[1]), 0))
    l_2.append((int(splitted[0]), int(splitted[1]), 0))

maxer_ind = 0
maxer = l_1[0][2]
for j in range (100):
    for i in range(len(l_1)):
        loger = math.log(l_1[i][0], 2)
        l_1[i] = (l_1[i][0], l_1[i][1], l_1[i][1] * loger)
        if (l_1[i][2] > maxer):
            maxer_ind = i
            maxer = l_1[i][2]

print("The solution is: " + str(maxer_ind+1))

print(f'Completed in {(time.perf_counter() - t0) * 1000:0.3f} ms')





