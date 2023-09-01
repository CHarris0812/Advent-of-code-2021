def part1():
    crabs = listOfCrabs()
    distances = []
    for i in range(2000):
        distances.append(calculateFuel(crabs, i))
    return min(distances)

def part2():
    crabs = listOfCrabs()
    distances = []
    for i in range(300, 500):
        distances.append(calculateFuelPart2(crabs, i))
        print(min(distances))
        print(i)
    return min(distances)

def listOfCrabs():
    f = open("AOC7.txt", "r")
    temp = f.readline()
    crabs = temp.split(",")
    crabs = [int(c) for c in crabs]
    return crabs

def calculateFuel(crabs, pos):
    count = 0
    for i in crabs:
        count += abs(i - pos)
    return count

def calculateFuelPart2(crabs, pos):
    count = 0
    for i in crabs:
        count += fuelToPos(i, pos)
    return count

def fuelToPos(crab, pos):
    dist = abs(crab - pos)
    count = 0
    for i in range(1, dist + 1):
        count += i
    return count

if __name__ == "__main__":
    #print(part1())
    print(part2())
