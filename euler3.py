def is_prime(x):
    for i in range (2,x//2+1):
        if (x%i ==0):
            return False
    return True

x = 59569

408464633
10086647
5753023
1234169
486847
104441
59569
6857
1471
839
71

for i in range (1,x):
    if (i%10000000 == 0):
        print(x/i)
    if (x%i ==0):
        if (is_prime(i)):
            print(str(i) + " is prime")
        else:
            print(str(i) + " is not prime")
#1 71 839 1471 6857

