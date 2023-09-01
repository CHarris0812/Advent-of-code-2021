import heapq

def part1():
    maze = readFile()
    visited = [[False for i in range(len(maze))] for j in range(len(maze))]
    shortest = findEnd(maze, visited)
    return shortest

def part2():
    maze = readFile()
    maze = makeBigMaze(maze)
    display(maze)
    visited = [[False for i in range(len(maze))] for j in range(len(maze))]
    shortest = findEnd(maze, visited)
    return shortest

def readFile():
    result = []
    f = open("AOC15.txt", "r")
    for line in f:
        temp = []
        line = line.replace("\n", "")
        for char in line:
            temp.append(int(char))
        result.append(temp)
    return result

def display(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            #temp = 1 if list[i][j] == True else 0
            #print(temp, end = "")
            print(list[i][j], end = "")
        print("")

def findEnd(maze, visited):
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0, 0))
    while(len(heap) > 0):
        temp = heapq.heappop(heap)
        if not visited[temp[1]][temp[2]]:
            visited[temp[1]][temp[2]] = True
            if temp[1] == temp[2] == len(maze) - 1:
                return temp[0]
            moves = possibilities(temp[1], temp[2], visited)
            for i in moves:
                if not visited[i[0]][i[1]]:
                    heapq.heappush(heap, (temp[0] + maze[i[0]][i[1]], i[0], i[1]))

def possibilities(row, col, visited):
    toReturn = []
    if row < len(visited) - 1 and not visited[row + 1][col]:
        toReturn.append((row + 1, col))
    if col < len(visited) - 1 and not visited[row][col + 1]:
        toReturn.append((row, col + 1))
    if row > 0 and not visited[row - 1][col]:
        toReturn.append((row - 1, col))
    if col > 0 and not visited[row][col - 1]:
        toReturn.append((row, col - 1))
    
    return toReturn

def makeBigMaze(maze):
    bigmaze = []
    for i in range(len(maze)):
        row = maze[i]
        temp = maze[i]
        for j in range(4):
            temp = [k + 1 for k in temp]
            for k in range(len(temp)):
                if temp[k] == 10:
                    temp[k] = 1
            row = row + temp
        bigmaze.append(row)

    for i in range(4):
        temp = [[] for j in range(len(bigmaze[0]))]
        for j in range(len(maze)):
            temp[i * len(maze) + j] = [k + 1 for k in bigmaze[j + len(maze) * i]]
        bigmaze = bigmaze + temp
    return bigmaze

if __name__ == "__main__":
    print(part1())
    #print(part2())
