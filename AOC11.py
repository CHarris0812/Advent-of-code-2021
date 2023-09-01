octoGrid = []
hasFlashed = []

def part1():
    global octoGrid
    global hasFlashed
    octoGrid = makeGrid()
    flashes = 0
    for i in range(100):
        hasFlashed = arrayOfFalse()
        addOne()
        for j in range(20):
            flashes += flashAll()
        removeFlashed()
    return flashes

def part2():
    global octoGrid
    global hasFlashed
    octoGrid = makeGrid()
    flashes = 0
    count = 0
    while True:
        count += 1
        hasFlashed = arrayOfFalse()
        addOne()
        for j in range(20):
            flashes += flashAll()
        if flashes == 100:
            return count
        removeFlashed()
        flashes = 0

def makeGrid():
    toReturn = []
    f = open("AOC11.txt", "r")
    for line in f:
        temp = []
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        for char in line:
            temp.append(int(char))
        toReturn.append(temp)
    return toReturn

def addOne():
    global octoGrid
    for i in range(10):
        for j in range(10):
            octoGrid[i][j] += 1

def flashAll():
    global octoGrid
    global hasFlashed
    flashes = 0

    for i in range(10):
        for j in range(10):
            if not hasFlashed[i][j] and octoGrid[i][j] > 9:
                flashes += 1
                hasFlashed[i][j] = True
                flash(i, j)
    return flashes

def arrayOfFalse():
    toReturn = []
    for i in range(10):
        temp = []
        for j in range(10):
            temp.append(False)
        toReturn.append(temp)
    return toReturn

def removeFlashed():
    global octoGrid
    global hasFlashed
    for i in range(10):
        for j in range(10):
            if hasFlashed[i][j]:
                octoGrid[i][j] = 0

def flash(row, col):
    global octoGrid
    if row > 0:
        octoGrid[row - 1][col] += 1
        if col > 0:
            octoGrid[row - 1][col - 1] += 1
        if col < 9:
            octoGrid[row - 1][col + 1] += 1
    if row < 9:
        octoGrid[row + 1][col] += 1
        if col > 0:
            octoGrid[row + 1][col - 1] += 1
        if col < 9:
            octoGrid[row + 1][col + 1] += 1
    if col > 0:
        octoGrid[row][col - 1] += 1
    if col < 9:
        octoGrid[row][col + 1] += 1

if __name__ == "__main__":
    print(part1())
    print(part2())
