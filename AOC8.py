def part1():
    data = readFromFile()
    count = 0
    for i in data:
        temp = i[1].split(" ")
        for j in temp:
            if len(j) in [2, 3, 4, 7]:
                count += 1
    return count

def part2():
    data = readFromFile()
    result = 0
    for i in data:
        base = {}
        strToVal = {}
        for j in i[0].split(" "):
            j = sorted(j)
            j = ''.join(j)
            j = j.replace(" ", "")
            if len(j) == 2:
                base[1] = j
                strToVal[j] = 1
            if len(j) == 3:
                base[7] = j
                strToVal[j] = 7
            if len(j) == 4:
                base[4] = j
                strToVal[j] = 4
            if len(j) == 7:
                base[8] = j
                strToVal[j] = 8

        for j in i[0].split(" "):
            j = sorted(j)
            j = ''.join(j)
            j = j.replace(" ", "")
            if len(j) == 6:
                if base[1][0] in j and base[1][1] in j:
                    count = 0
                    for k in base[4]:
                        if k in j:
                            count += 1
                    if count == 3:
                        strToVal[j] = 0
                    else:
                        strToVal[j] = 9
                else:
                    strToVal[j] = 6

            if len(j) == 5:
                count = 0
                for k in base[1]:
                    if k in j:
                        count += 1
                if count == 2:
                    strToVal[j] = 3

                else:
                    count = 0
                    for k in base[4]:
                        if k in j:
                            count += 1
                    if count == 3:
                        strToVal[j] = 5
                    else:
                        strToVal[j] = 2

        count = 0
        for j in i[1].split(" "):
            j = sorted(j)
            j = ''.join(j)
            j = j.replace(" ", "")
            count = count * 10 + strToVal[j]
        print(count)
        result += count
    return result

def readFromFile():
    f = open("AOC8.txt", "r")
    data = []
    for line in f:
        line = line.replace("\n", "")
        data.append(line.split(" | "))
    return data

if __name__ == "__main__":
    print(part1())
    print(part2())
