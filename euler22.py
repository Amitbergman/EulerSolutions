def getSumOfWord(name):
    l = [ord(i) - 96 for i in name]
    return sum(l)

listOfNames = []
with open('p22.txt','r') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split(","):
            # dremoving the " from the start and end of the name         
            currentName = word[1:-1].lower()
            listOfNames.append(currentName)

sortedListOfNames = sorted(listOfNames)
index = 1
sumOfAll = 0
for i in sortedListOfNames:
    sumOfAll += index * getSumOfWord(i)
    index +=1

print(sumOfAll)