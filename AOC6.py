def part1():
    fish = createDict()
    print(fish)
    for i in range(256):
        fish = nextDay(fish)
        print(fish)
    return countFish(fish)

def part2():
    return

def createDict():
    f = open("AOC6.txt", "r")
    line = f.readline()
    result = {}
    for i in range(9):
        result[i] = line.count(str(i))
    return result

def nextDay(fish):
    temp = fish[0]
    for i in range(8):
        fish[i] = fish[i + 1]
    fish[8] = temp
    fish[6] += temp
    return fish

def countFish(fish):
    count = 0
    for i in range(9):
        count += fish[i]
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())
