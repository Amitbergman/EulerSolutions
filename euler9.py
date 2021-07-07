def isPitagorian(a,b,c):
    if (c < 5 or c ==b or c ==a or a == b):
        return False
    return a**2 + b**2 == c**2

for a in range(1000):
    for b in range(a,1000):
        c = 1000 - a - b
        if (isPitagorian(a,b,c)):
            print(a,b,c)
            print("Solution is:", a*b*c)