def part1():
    targetX = [x for x in range(135, 156)]
    targetY = [y for y in range(-102, -77)]
    possibleX = {}
    max = 0
    for x in range(100):
        for y in range(100):
            hit = hitTarget(x, y, targetX, targetY)
            if hit:
                maxH = maxHeight(y)
                if maxH > max:
                    max = maxH
                    print(max)
    return max

def hitTarget(x, y, targetX, targetY):
    xPos = 0
    yPos = 0
    while xPos <= max(targetX) and yPos >= min(targetY):
        xPos += x
        yPos += y
        if inTarget(xPos, yPos, targetX, targetY):
            return True
        y -= 1
        if x > 0:
            x -= 1
    return False

def maxHeight(y):
    max = 0
    while y > 0:
        max += y
        y -= 1
    return max

def inTarget(x, y, xTarget, yTarget):
    return x in xTarget and y in yTarget

def getHeight(velo, steps):
    max = 0
    total = 0
    for i in range(steps):
        total += velo
        if total > max:
            max = total
        velo -= 1
    return max, total

def hitsTargetX(x, targetX):
    steps = 0
    xPos = 0
    hits = []
    while xPos <= max(targetX) and x > 0:
        xPos += x
        steps += 1
        x -= 1
        if inTarget(xPos, targetX):
            hits.append(steps)
    if inTarget(xPos, targetX):
        for i in range(10):
            steps += 1
            hits.append(steps)
    return hits

if __name__ == "__main__":
    print(part1())
    #print(part2())

