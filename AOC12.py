def part1():
    dict, small = makeDict()
    paths = recursive_backtracking("start", dict, small)
    return paths

def part2():
    dict, small = makeDict2()
    paths = recursive_backtracking2("start", dict, small, False)
    return paths

def makeDict():
    f = open("AOC12.txt", "r")
    dict = {}
    small = {}
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for line in f:
        line = line.replace("\n", "")
        line = line.split("-")
        if line[0] in dict:
            dict[line[0]] = dict[line[0]] + [line[1]]
        else:
            dict[line[0]] = [line[1]]

        if line[1] in dict:
            dict[line[1]] = dict[line[1]] + [line[0]]
        else:
            dict[line[1]] = [line[0]]

        for i in range(2):
            if line[i][0] in lowercase and line[i] not in ["start", "end"]:
                small[line[i]] = False
    return dict, small

def makeDict2():
    f = open("AOC12.txt", "r")
    dict = {}
    small = {}
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for line in f:
        line = line.replace("\n", "")
        line = line.split("-")
        if line[0] in dict:
            dict[line[0]] = dict[line[0]] + [line[1]]
        else:
            dict[line[0]] = [line[1]]

        if line[1] in dict:
            dict[line[1]] = dict[line[1]] + [line[0]]
        else:
            dict[line[1]] = [line[0]]

        for i in range(2):
            if line[i][0] in lowercase and line[i] not in ["start", "end"]:
                small[line[i]] = 0
    return dict, small

def copyDict(dict):
    tempDict = {}
    for i in dict:
        tempDict[i] = dict[i]
    return tempDict

def recursive_backtracking(key, dict, small):
    if key == "end":
        return 1

    paths = 0
    for val in dict[key]:
        tempSmall = copyDict(small)
        if val != "start":
            if val in tempSmall:
                if tempSmall[val] == False:
                    tempSmall[val] = True
                    paths += recursive_backtracking(val, dict, tempSmall)
            else:
                paths += recursive_backtracking(val, dict, tempSmall)
    return paths

def recursive_backtracking2(key, dict, small, two):
    if key == "end":
        return 1

    paths = 0
    for val in dict[key]:
        tempSmall = copyDict(small)
        if val != "start":
            if val in tempSmall:
                if tempSmall[val] == 0:
                    tempSmall[val] = 1
                    paths += recursive_backtracking2(val, dict, tempSmall, two)
                elif tempSmall[val] == 1:
                    if not two:
                        tempSmall[val] = 2
                        paths += recursive_backtracking2(val, dict, tempSmall, True)
            else:
                paths += recursive_backtracking2(val, dict, tempSmall, two)
    return paths

if __name__ == "__main__":
    print(part1())
    print(part2())