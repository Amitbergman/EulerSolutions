f = open("C:\\Users\\ambergma\\Desktop\\Amit\\Project euler\\euler_99\\p099_base_exp.txt", "r")
import math
def greater(l,i,j):
    return l[i][0] > l[j][0] and l[i][1] > l[j][1]

l_1 = list()
l_2 = list()
a = 0
for x in f:
    splitted = x.split(",")

    l_1.append((int(splitted[0]), int(splitted[1]), 0))
    l_2.append((int(splitted[0]), int(splitted[1]), 0))

for j in range (100):
    for i in range(len(l_1)):
        loger = math.log(l_1[i][0], 2)
        l_1[i] = (l_1[i][0], l_1[i][1], l_1[i][1] * loger)
maxer_ind = 0
maxer = l_1[0][2]
for i in range(len(l_1)):
    if (l_1[i][2] > maxer):
        maxer_ind = i
        maxer = l_1[i][2]

print(maxer_ind)
print(l_2[maxer_ind])






