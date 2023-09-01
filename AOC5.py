def part1():
    board = makeEmptyBoard()
    f = open("AOC5.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        temp = line.split(" -> ")
        line1 = temp[0].split(",")
        line2 = temp[1].split(",")
        line1 = [int(line1[0]), int(line1[1])]
        line2 = [int(line2[0]), int(line2[1])]
        if line1[0] == line2[0]:
            board = drawRow(line1[1], line2[1], line1[0], board)
        elif line1[1] == line2[1]:
            board = drawColumn(line1[0], line2[0], line1[1], board)
    return sumGreaterThanOne(board)

def part2():
    board = makeEmptyBoard()
    f = open("AOC5.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        temp = line.split(" -> ")
        line1 = temp[0].split(",")
        line2 = temp[1].split(",")
        line1 = [int(line1[0]), int(line1[1])]
        line2 = [int(line2[0]), int(line2[1])]
        if line1[0] == line2[0]:
            board = drawRow(line1[1], line2[1], line1[0], board)
        elif line1[1] == line2[1]:
            board = drawColumn(line1[0], line2[0], line1[1], board)
        else:
            board = drawDiagonal(line1[1], line1[0], line2[1], line2[0], board)
    return sumGreaterThanOne(board)

def makeEmptyBoard(size = 1000):
    return [[0 for i in range(size)] for i in range(size)]

def drawColumn(y1, y2, x, board):
    for i in range(len(board)):
        if i >= min(y1, y2) and i <= max(y1, y2):
            board[i][x] += 1
    return board

def drawRow(x1, x2, y, board):
    for i in range(len(board)):
        if i >= min(x1, x2) and i <= max(x1, x2):
            board[y][i] += 1
    return board

def drawDiagonal(y1, x1, y2, x2, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if i >= min(x1, x2) and i <= max(x1, x2) and j >= min(y1, y2) and j <= max(y1, y2):
                if abs(x1 - i) == abs(y1 - j) and abs(x2 - i) == abs(y2 - j):
                    board[i][j] += 1
    return board

def sumGreaterThanOne(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 1:
                count += 1
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())
