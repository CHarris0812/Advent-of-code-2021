global inBasin

def part1():#100x100
    result = 0
    data = readFile()
    for char in range(len(data)):
        adj = findAdjacents(char, data)
        lowest = True
        for val in adj:
            if val <= int(data[char]):
                lowest = False
        if lowest:
            result += int(data[char]) + 1
    return result

def part2():
    global inBasin
    data = readFile()
    inBasin = ''.join(["0" for i in range(10000)])
    inBasin = inBasin.replace(" ", "")
    for i in range(len(data)):
        if data[i] == "9":
            inBasin = inBasin[:i] + "1" + inBasin[i+1:]
    
    basins = []
    for i in range(len(data)):
        if inBasin[i] == "0":
            basins.append(findBasin(i, data))

    vals = threeBiggestValues(basins)
    return vals[0] * vals[1] * vals[2]

def readFile():
    f = open("AOC9.txt", "r")
    temp = ""
    for line in f:
        temp += line
    temp = temp.replace(" ", "")
    temp = temp.replace("\n", "")
    return temp

def findAdjacents(loc, data):
    adj = []
    if loc % 100 != 0:
        adj.append(int(data[loc - 1]))
    if loc % 100 != 99:
        adj.append(int(data[loc + 1]))

    if loc // 100 != 0:
        adj.append(int(data[loc - 100]))
    if loc // 100 != 99:
        adj.append(int(data[loc + 100]))
    return adj

def findAdjacentsLocation(loc, data):
    adj = []
    if loc % 100 != 0:
        adj.append(loc - 1)
    if loc % 100 != 99:
        adj.append(loc + 1)

    if loc // 100 != 0:
        adj.append(loc - 100)
    if loc // 100 != 99:
        adj.append(loc + 100)
    return adj

def findBasin(loc, data):
    global inBasin
    inBasin = inBasin[:loc] + "1" + inBasin[loc + 1:]
    result = 1
    for i in findAdjacentsLocation(loc, data):
        if inBasin[i] == "0":
            result += findBasin(i, data)
    return result

def threeBiggestValues(basins):
    vals = []
    print(basins)
    for i in range(3):
        maxVal = max(basins)
        vals.append(maxVal)
        basins.remove(maxVal)
    return vals

if __name__ == "__main__":
    print(part1())
    print(part2())
