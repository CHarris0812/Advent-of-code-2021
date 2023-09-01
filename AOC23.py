import heapq

def generateNeighbors():
    '''
    # # # # # # # # # # # # #
    # 0 1 2 3 4 5 6 7 8 9 10#
    # # # 11 #15 #19 #23 # ##
        # 12 #16 #20 #24 #
        # 13 #17 #21 #25 #
        # 14 #18 #22 #26 #
        # # # # # # # # #
    '''
    neighbors = {}
    neighbors[0] = [1]
    neighbors[1] = [0, 2]
    neighbors[2] = [1, 3, 11]
    neighbors[3] = [2, 4]
    neighbors[4] = [3, 5, 15]
    neighbors[5] = [4, 6]
    neighbors[6] = [5, 7, 19]
    neighbors[7] = [6, 8]
    neighbors[8] = [7, 9, 23]
    neighbors[9] = [8, 10]
    neighbors[10] = [9]
    neighbors[11] = [2, 12]
    neighbors[12] = [11, 13]
    neighbors[13] = [12, 14]
    neighbors[14] = [13]
    neighbors[15] = [4, 16]
    neighbors[16] = [15, 17]
    neighbors[17] = [16, 18]
    neighbors[18] = [17]
    neighbors[19] = [6, 20]
    neighbors[20] = [19, 21]
    neighbors[21] = [20, 22]
    neighbors[22] = [21]
    neighbors[23] = [8, 24]
    neighbors[24] = [23, 25]
    neighbors[25] = [24, 26]
    neighbors[26] = [25]
    return neighbors

def generatePossibilities(cost, state, neighbors):
    possible = []
    notOutsideDoor = [0, 1, 3, 5, 7, 9, 10]
    hall = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    costToMove = {"A":1, "B":10, "C":100, "D":1000}
    for i in range(27):
        if state[i] != ".":
            temp = canMoveIntoRoom(state, neighbors, i)
            if temp[0]:
                return [(cost + temp[1], temp[2])]

    for i in range(27):
        if state[i] != "." and i not in hall:
            for j in range(27):
                if i != j and state[j] == "." and j in notOutsideDoor:
                    temp = state[i]
                    path = findPath(i, j, generateNeighbors())
                    if isValid(state, path):
                        possible.append((cost + len(path) * costToMove[temp], swap(state, i, j)))
    return possible

def generateDestinations(piece):
    destinations = {}
    destinations["A"] = [11, 12, 13, 14]
    destinations["B"] = [15, 16, 17, 18]
    destinations["C"] = [19, 20, 21, 22]
    destinations["D"] = [23, 24, 25, 26]
    return destinations[piece]

def isValid(state, path):
    for i in path:
        if state[i] != ".":
            return False
    return True

def findPath(start, goal, neighbors):
    temp = generatePath(start, goal, neighbors)
    temp.remove(temp[0])
    return temp

def generatePath(start, goal, neighbors):
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, [start]))
    while len(heap) > 0:
        temp = heapq.heappop(heap)
        if temp[1][len(temp[1]) - 1] == goal:
            return temp[1]
        for i in neighbors[temp[1][len(temp[1]) - 1]]:
            heapq.heappush(heap, (temp[0] + 1, temp[1] + [i]))
    return move

def minVal(moves):
    min = 1000
    minVal = -1
    for i in moves:
        if len(str(i)) < min:
            min = len(str(i))
            minVal = i
    return minVal

def canMoveIntoRoom(state, neighbors, pos):
    costToMove = {"A":1, "B":10, "C":100, "D":1000}
    myPiece = state[pos]
    goal = generateDestinations(myPiece)
    if myPiece == ".":
        return (False, -1, -1)
    index = -1
    if pos in goal:
        index = goal.index(pos)
    for i in range(3, index, -1):
        path = findPath(pos, goal[i], neighbors)
        if isValid(state, path):
            return (True, len(path) * costToMove[myPiece], swap(state, pos, path[len(path) - 1]))
    return (False, -1, -1)

def swap(state, pos1, pos2):
    temp = state[pos1]
    state = state[:pos1] + state[pos2] + state[pos1 + 1:]
    state = state[:pos2] + temp + state[pos2 + 1:]
    return state

def part1():
    neighbors = generateNeighbors()
    #initialState = "...........CCAABDDB"
    initialState = "...........DDDBDCBACBABCACA"
    heap = [(0, initialState)]
    goal = "...........AAAABBBBCCCCDDDD"
    heapq.heapify(heap)
    alreadyReached = []
    count = 0
    while len(heap) > 0:
        
        temp = heapq.heappop(heap)
        print(temp)
        if temp[0] == 2060:
            print("eeee")
        if temp[1] == goal:
            return temp
        if temp[1] not in alreadyReached:
            alreadyReached.append(temp[1])
            possibleMoves = generatePossibilities(temp[0], temp[1], neighbors)
            for i in possibleMoves:
                if i[1] not in alreadyReached:
                    heapq.heappush(heap, (i[0], i[1]))

if __name__ == "__main__":
    #print(findPath(8, 16, generateNeighbors()))
    print(part1())
    #print(generatePossibilities(2060, 'AA.......D.CC.B.D.B', generateNeighbors()))
