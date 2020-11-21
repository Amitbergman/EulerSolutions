def greater(l,i,j):
    return l[i][0] > l[j][0] and l[i][1] > l[j][1]

f = open("C:\\Users\\ambergma\\Desktop\\Amit\\Project euler\\euler_99\\p099_base_exp.txt", "r")
import time
import math
t0 = time.perf_counter()

index = 0
maxer_ind = 0
maxer = 1
for line in f:
    index = index + 1
    splitted_line = line.split(",")
    currentValue  = math.log(int(splitted_line[0]), 2) * int(splitted_line[1])
    if (currentValue > maxer):
        maxer_ind = index
        maxer = currentValue 

print("The solution is: " + str(maxer_ind))

print(f'Completed in {(time.perf_counter() - t0) * 1000:0.3f} ms')





