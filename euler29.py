start = 2
end = 100
l = []
for i in range(start, end+1):
    l.extend([i**k for k in range(start,end + 1)])
print(len(set(l)))
