
function isIncreasing(number){
    numAsStr = number.toString()
    var len = numAsStr.length
    if (len == 1){
        return true
    }
    if (numAsStr[len-1] >= numAsStr[len-2]){
        return isIncreasing(numAsStr.slice(0,-1))
    }
    return false
}

function isDecreasing(number){
    numAsStr = number.toString()
    var len = numAsStr.length
    if (len == 1){
        return true
    }
    if (numAsStr[len-1] <= numAsStr[len-2]){
        return isDecreasing(numAsStr.slice(0,-1))
    }
    return false
}

function isBouncy(number){
    return (!isDecreasing(number) && ! isIncreasing(number))
}

counter = 0
for (let i = 0; i < 1000; i++) {
    
    if (isBouncy(i)){
        counter ++
    }
}
console.log(counter, "should be 525")

percentage = 0
general = 0
bouncy = 0
toCheck = 1
goal = 0.99
while (percentage < goal){
    if (isBouncy(toCheck)){
        bouncy +=1
    }
    toCheck +=1
    general +=1
    percentage = bouncy / general
}
console.log("Answer to euler 112 is: ", general)