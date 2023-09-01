import time

def part1():
    result = "SFBBNKKOHHHPFOFFSPFV"
    dict = makeDict()
    steps = 10
    for i in range(steps):
        print(i)
        temp = ""
        final = ""
        for j in range(len(result) - 1):
            temp += dict[result[j:j+2]]
        for k in range(len(result) - 1):
            final += result[k]
            final += temp[k]
        final += result[-1]
        result = final
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = {i:result.count(i) for i in letters}
    print(counter)

    min = 10000000
    max = 0
    for i in counter:
        if counter[i] != 0:
            if counter[i] < min:
                min = counter[i]
            if counter[i] > max:
                max = counter[i]
    return max - min

def makeDict():
    dict = {}
    f = open("AOC14.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        line = line.split(" -> ")
        dict[line[0]] = line[1]
    return dict

def part2():
    result = "SFBBNKKOHHHPFOFFSPFV"
    dict = makeDict()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = {i:0 for i in letters}
    countOfPairs = {i:0 for i in dict}
    for i in range(len(result) - 1):
        countOfPairs[result[i:i + 2]] = countOfPairs[result[i:i + 2]] + 1
    for i in result:
        counter[i] = counter[i] + 1
    print(counter)
    steps = 40
    for i in range(steps):
        print(i)
        tempDict = {j:0 for j in dict}
        for j in countOfPairs:
            if countOfPairs[j] != 0:
                tempDict[j[0] + dict[j]] = tempDict[j[0] + dict[j]] + countOfPairs[j]
                tempDict[dict[j] + j[1]] = tempDict[dict[j] + j[1]] + countOfPairs[j]
                counter[dict[j]] = counter[dict[j]] + countOfPairs[j]
        countOfPairs = {k:tempDict[k] for k in tempDict}
        print(countOfPairs)
        print(counter)
    min = 10000000000000
    max = 0
    print(counter)
    for i in counter:
        if counter[i] != 0:
            if counter[i] < min:
                min = counter[i]
            if counter[i] > max:
                max = counter[i]
    return max - min

if __name__ == "__main__":
    #print(part1())
    print(part2())