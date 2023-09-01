def part1():
    instructions = readData()
    for i in range(100000000000000, 0, -1):
        if str(i).count("0") == 0:
            w = 0
            x = 0
            y = 0
            z = 0
            num = str(i)
            char = 0
            for line in data:
                temp = line[:3]
                if temp == "inp":
                    w = int(num[char])
                    char += 1
                var = line[4]
                val = line[6:]

def readData():
    f = open("AOC24.txt", "r")
    data = []
    for line in f:
        line = line.replace("\n", "")
        data.append(line)
    return data

if __name__ == "__main__":
    part1()