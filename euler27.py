import math

def is_prime(x):
    if (x <= 1):
        return False
    sqrt = math.sqrt(x)
    end = int(math.ceil(sqrt))
    for i in range (2,end+1):
        if (x%i ==0):
            return False
    return True

def evaluate(a,b, n):
    return n**2 + a * n + b

def numberOfConsecutivePrimes(a,b):
    n = 0
    to_check = evaluate(a,b,n)
    while(is_prime(to_check)):
        n +=1
        to_check = evaluate(a,b,n)
    return n
maxer = 0
max_a = 0
max_b = 0

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        current = numberOfConsecutivePrimes(a,b)
        if (current > maxer):
            max_a = a
            max_b = b
            maxer = current

print("Solution is {}".format(max_b  * max_a))