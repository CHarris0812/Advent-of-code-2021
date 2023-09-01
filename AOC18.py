import math

def part1():
    data = readFile()
    values = data[0]
    for i in range(1, len(data)):
        values = addAndModify(values, data[i])
    return magnitude(values)

def part2():
    data = readFile()
    max = 0
    for i in range(len(data)):
        for j in range(len(data)):
            temp = addAndModify(data[i], data[j])
            val = magnitude(temp)
            if val > max:
                max = val
    return max

def addAndModify(num1, num2):
    values = add(num1, num2)
    values = explodeRepeatedly(values)
    temp = splitAndExplode(values)
    while temp != values:
        values = ''.join(temp)
        temp = splitAndExplode(values)
    values = ''.join(temp)
    return values

def readFile():
    data = []
    f = open("AOC18.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        data.append(line)
    return data

def splitAndExplode(values):
    values = split(values)
    values = explodeRepeatedly(values)
    return values

def explodeRepeatedly(values):
    temp = explode(values)
    while temp != values:
        values = ''.join(temp)
        temp = explode(temp)
    values = ''.join(temp)
    return values

def explode(values):
    countOpen = 0
    hasExploded = False
    for i in range(len(values)):
        if not hasExploded:
            if values[i] == "[":
                countOpen += 1
            elif values[i] == "]":
                countOpen -= 1
            else:
                if countOpen > 4:
                    prevOpen = i - 1
                    nextClose = -1
                    for j in range(i, len(values)):
                        if values[j] == "]" and nextClose == -1:
                            nextClose = j
                    prevNum = -1
                    for j in range(i - 1, 0, -1):
                        if values[j] in "1234567890":
                            prevNum = (j, j + 1)
                            stillNumber = True
                            for k in range(1, 10):
                                stillNumber = values[j - k] in "1234567890"
                                if stillNumber:
                                    prevNum = (j - k, j + 1)
                                else:
                                    break
                            break
                    nextNum = -1
                    for j in range(nextClose, len(values)):
                        if values[j] in "1234567890":
                            nextNum = (j, j + 1)
                            stillNumber = True
                            for k in range(1, 10):
                                stillNumber = values[j + k] in "1234567890"
                                if stillNumber:
                                    nextNum = (j, j + 1 + k)
                                else:
                                    break
                            break
                    tempVals = values[prevOpen + 1 : nextClose].split(",")
                    val0 = int(tempVals[0])
                    val1 = int(tempVals[1])
                    if prevNum == -1:
                        if nextNum == -1:
                            values = values[:prevOpen] + "0" + values[nextClose + 1:]
                        else:
                            values = values[:prevOpen] + "0" + values[nextClose + 1 : nextNum[0]] + str(int(values[nextNum[0] : nextNum[1]]) + val1) + values[nextNum[1]:]
                    elif nextNum == -1:
                        values = values[:prevNum[0]] + str(int(values[prevNum[0] : prevNum[1]]) + val0) + values[prevNum[1] : prevOpen] + "0" + values[nextClose + 1:]
                    else:
                        values = values[:prevNum[0]] + str(int(values[prevNum[0] : prevNum[1]]) + val0) + values[prevNum[1] : prevOpen] + "0" + values[nextClose + 1 : nextNum[0]] + str(int(values[nextNum[0] : nextNum[1]]) + val1) + values[nextNum[1]:]
                    return values
    return values

def split(values):
    hasSplit = False
    for i in range(len(values)):
        if not hasSplit:
            if values[i] in "1234567890":
                if values[i + 1] in "1234567890":
                    temp = 2
                    if values[i + 2] in "1234567890":
                        temp = 3
                    values = values[:i] + "[" + str(math.floor(int(values[i:i+temp]) / 2.0)) + "," + str(math.ceil(int(values[i:i+temp]) / 2.0)) + "]" + values[i+temp:]
                    return values
    return values

def add(num1, num2):
    if not (type(num1) is str and type(num2) is str):
        print("error")
    return "[" + num1 + "," + num2 + "]"

def magnitude(values):
    if values.count("[") == 0:
        return int(values)
    if values.count("[") == 1:
        values = values.replace("[", "")
        values = values.replace("]", "")
        values = values.split(",")
        return int(values[0]) * 3 + int(values[1]) * 2
    temp = ''.join(values)
    countOpen = 1
    leftPair = ""
    leftFound = False
    rightPair = ""
    temp = temp[1:]
    if temp[0] in "1234567890":
        leftPair = temp[0]
        rightPair = temp[2:len(temp) - 1]
        leftFound = True
    else:
        temp = temp[1:]
        for i in temp:
            if not leftFound:
                if i == "[":
                    countOpen += 1
                if i == "]":
                    countOpen -= 1
                leftPair += i
                if countOpen == 0:
                    leftFound = True
            else:
                rightPair += i
        leftPair = "[" + leftPair
        rightPair = rightPair[1:len(rightPair) - 1]
    leftValue = 3 * magnitude(leftPair)
    rightValue = 2 * magnitude(rightPair)
    return leftValue + rightValue

if __name__ == "__main__":
    print(part1())
    print(part2())
