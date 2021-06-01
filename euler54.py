d = dict()
for i in range(2,11):
    d[str(i)] = i
d["J"] = 11
d["Q"] = 12
d["K"] = 13
d["A"] = 14
d["T"] = 10

HIGH_CARD = 0
PAIR = 1
TWO_Pairs = 2
ThreeOfAKind = 3
Straight = 4
Flush = 5
FullHouse = 6
FourOfAKind = 7
StraightFlush = 8

def split_to_2_hands(hands):
    splitted = hands.split(" ")
    hand_1 = splitted[:5]
    hand_2 = splitted[5:]
    return (hand_1, hand_2)


def getNumbersArray(hand):
    l = []
    for i in hand:
        l.append(d[i[0]])
    return l

def getColorsArray(hand):
    return [a[1] for a in hand]

def hasFlush(hand):
    colors = getColorsArray(hand)
    return (colors.count(colors[0]) == 5)

def highCard(hand):
    return max(getNumbersArray(hand))

def hasStraight(hand):
    numbers = sorted(getNumbersArray(hand))
    minimal = numbers[0]
    for i in range(1,4):
        if (numbers[i] != minimal + i):
            return False
    if (minimal == 2):
        if (numbers[4] == 14 or numbers [4] == 6):
            return True
        return False
    else:
        if (numbers[4] == minimal + 4):
            return True
        return False

def has4OfAKind(hand):
    numbers = getNumbersArray(hand)
    for i in numbers:
        if (numbers.count(i) == 4):
            return True
    return False

def has2pairs(hand):
    numbers = getNumbersArray(hand)
    l = set()
    for i in numbers:
        if (numbers.count(i) == 2):
            l.add(i)
    return len(l) == 2

def highestCard(hand):
    numbers = getNumbersArray(hand)
    return max(numbers)

def highestPair(hand):
    numbers = getNumbersArray(hand)
    maxPair = 0
    for i in numbers:
        if (numbers.count(i) == 2 and i > maxPair):
            maxPair = i
    return maxPair

def highestCardNotInPair(hand):
    numbers = getNumbersArray(hand)
    maxNotInPair = 0
    for i in numbers:
        if (numbers.count(i) == 1 and i > maxNotInPair):
            maxNotInPair = i
    return maxNotInPair

def hasPair(hand):
    numbers = getNumbersArray(hand)
    l = set()
    for i in numbers:
        if (numbers.count(i) == 2):
            l.add(i)
    return len(l) == 1

def has3OfAKind(hand):
    numbers = getNumbersArray(hand)
    for i in numbers:
        if (numbers.count(i) == 3):
            return True
    return False

def hasFullHouse(hand):
    three = False
    two = False
    numbers = getNumbersArray(hand)
    for i in numbers:
        if (numbers.count(i) == 3):
            three = True
        if (numbers.count(i) == 2):
            two = True
    return three and two


def WhatHeHas(hand):
    if (hasFlush(hand) and hasStraight(hand)):
        return StraightFlush #Not happening in the data set
    if (has4OfAKind(hand)):
        return FourOfAKind #Not happening in the date set
    if (hasFullHouse(hand)):
        return FullHouse #There is no full house against full house in the data set
    if (hasFlush(hand)):
        return Flush #There is no flush against flush in the data set
    if (hasStraight(hand)):
        return Straight #There is no straight against straight in the data set
    if (has3OfAKind(hand)):
        return ThreeOfAKind #There is no three of a kind against three of a kind in the data set
    if (has2pairs(hand)):
        return TWO_Pairs
    if (hasPair(hand)):
        return PAIR + highestPair(hand) / 100
    return highestCard(hand) / 100

def whoWins(hand_1, hand_2):
    first = WhatHeHas(hand_1)
    second = WhatHeHas(hand_2)
    if (first > second):
        return 1
    if (second > first):
        return 2
    # The only ties in the data set are between pairs
    if ( PAIR<=first< TWO_Pairs  and PAIR<=second < TWO_Pairs):
        first = highestCardNotInPair(hand_1)
        second = highestCardNotInPair(hand_2)
        if (first > second):
            return 1
        if (second > first):
            return 2
    return 0

f = open("p054_poker.txt", "r")
results = []
for x in f:
    (hand_1, hand_2) = split_to_2_hands(x)
    results.append(whoWins(hand_1, hand_2))
print("Solution to euler 54 is " + str(results.count(1)))

f.close()