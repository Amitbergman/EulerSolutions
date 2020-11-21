def is_prime(x):
    for i in range (2,x//2+1):
        if (x%i ==0):
            return False
    return True

x = 6857

for i in range (1,x):
    if (x%i ==0):
        if (is_prime(i)):
            print(i)
#1 71 839 1471

