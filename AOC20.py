def part1():
    data = readFromFile()
    for i in range(25):
        data = addZeroes(data)
        data = enhance(data)
        data[0] = ["#" for i in range(len(data))]
        data[len(data) - 1] = ["#" for i in range(len(data))]
        for i in range(len(data)):
            data[i][0] = "#"
            data[i][len(data) - 1] = "#"
        data = addZeroes(data, "#")
        data = enhance(data)
        for i in range(len(data)):
            data[i][0] = "."
            data[i][len(data) - 1] = "."
        data[0] = ["." for i in range(len(data))]
        data[len(data) - 1] = ["." for i in range(len(data))]
    return sum(data[i].count("#") for i in range(len(data)))

def readFromFile():
    data = []
    f = open("AOC20.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        data.append([c for c in line])
    return data

def addZeroes(data, char = "."):
    extraZeroes = 2
    toReturn = []
    for j in range(extraZeroes):
        toReturn.append([char for i in range(len(data) + extraZeroes * 2)])
    for i in range(len(data)):
        toReturn.append([char for j in range(extraZeroes)] + [c for c in data[i]] + [char for j in range(extraZeroes)])
    for j in range(extraZeroes):
        toReturn.append([char for i in range(len(data) + extraZeroes * 2)])
    return toReturn

def enhance(data):
    temp = []
    for i in range(len(data)):
        temp.append(["." for j in range(len(data))])

    for i in range(len(data) - 2):
        for j in range(len(data) - 2):
            temp[i + 1][j + 1] = enhancePixel(i + 1, j + 1, data)
    return temp

def enhancePixel(row, col, data):
    temp = ""
    enhanceString = "####.#.#..####.#.####..#..#####.....#####.###..##.##......###.###.#.....####....####..##.##..####..........##.##...#..##..#.#.###..##...#....#...#..###.#.#####..#..#...#.####..####.#..##.#.#.###.##.##.....###..##....#....#.#.###.##.#..#..#..#######.#.##.#...#....#.....#.#..#.#.##.##.######.#..##.#..##..#####..#..###...##.#.###.#.#..###..###.....####....##...#.####.###.#.#.#..#..##.#..#.##.#.#####.####.#.#...##.####.#######...#....#####.##.#......##.######..###.###...##.##..##..#.#..####.##..#..##.#...#..#.."
    #enhanceString = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
    for i in range(-1, 2):
        for j in range(-1, 2):
            temp += data[row + i][col + j]
    binary = ""
    for char in temp:
        binary += "0" if char == "." else "1"
    index = int(binary, 2)
    return enhanceString[index]


if __name__ == "__main__":
    print(part1())
    #print(part2())
