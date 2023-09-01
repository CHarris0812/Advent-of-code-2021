def part1():
    numbers = getNumbers()
    boards = getBoards()
    numbersCalled = getNumbersCalled()
    
    for i in numbers:
        for b in range(100):
            numbersCalled[b] = callNumber(boards[b], numbersCalled[b], i)
        for b in range(100):
            if checkComplete(numbersCalled[b]):
                return count(boards[b], numbersCalled[b]) * i

def part2():
    numbers = getNumbers()
    boards = getBoards()
    numbersCalled = getNumbersCalled()
    possibilities = [1 for i in range(100)]

    for i in numbers:
        for b in range(100):
            numbersCalled[b] = callNumber(boards[b], numbersCalled[b], i)
        for b in range(100):
            if checkComplete(numbersCalled[b]):
                if sum(possibilities) == 1:
                    if possibilities[b] == 1:
                        return count(boards[b], numbersCalled[b]) * i
                else:
                    possibilities[b] = 0

def getNumbers():
    numbers = "49,48,98,84,71,59,37,36,6,21,46,30,5,33,3,62,63,45,43,35,65,77,57,75,19,44,4,76,88,92,12,27,7,51,14,72,96,9,0,17,83,64,38,95,54,20,1,74,69,80,81,56,10,68,42,15,99,53,93,94,47,13,29,34,60,41,82,90,25,85,78,91,32,70,58,28,61,24,55,87,39,11,79,50,22,8,89,26,16,2,73,23,18,66,52,31,86,97,67,40"
    numbers = numbers.split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers

def getBoards():
    boards = []
    f = open("AOC4.txt", "r")
    for i in range(100):
        b = []
        for j in range(5):
            line = f.readline()
            line = line.replace("\n", "")
            row = line.split(" ")
            row2 = []
            for k in row:
                if k != "":
                    row2.append(int(k))
            b.append(row2)
        f.readline()
        boards.append(b)
    return boards

def getNumbersCalled():
    numbersCalled = []
    for i in range(100):
        b = []
        for j in range(5):
            b.append([1, 1, 1, 1, 1])
        numbersCalled.append(b)
    return numbersCalled

def callNumber(board, called, number):
     for i in range(5):
         for j in range(5):
             if board[i][j] == number:
                 called[i][j] = 0
     return called

def checkComplete(numbers):
    for i in numbers:
        if sum(i) == 0:#rows
            return True

    for i in range(5):#columns
        if numbers[0][i] + numbers[1][i] + numbers[2][i] + numbers[3][i] + numbers[4][i] == 0:
            return True
    return False

def count(board, called):
    count = 0
    for i in range(5):
        for j in range(5):
            count += board[i][j] * called[i][j]
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())