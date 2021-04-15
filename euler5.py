#We of course need all the primes:

res = 2*3*5*7*11*13*17*19
print(res)
# to get 4 we need to add another 2
res = res * 2
# we already have 6 (2*3)
# we already have 7
# to get 8 we need another 2
res = res * 2
# to get 9 we need another 3
res = res * 3
# we already have 10 (5*2)
# we already have 11
# we already have 12 (2*3*2)
# we already have 13
# we already have 14 (7*2)
# we already have 5 (5*3)
# to get 16 we need another 2 (2*2*2*2)
res = res * 2
# we already have 17
# we already have 18 (3*3*2)
# we already have 19
# we already have 20 (5*2*2)

print(res)

