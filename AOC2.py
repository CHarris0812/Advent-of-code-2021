def main():
    horizontal = 0
    vertical = 0
    aim = 0
    f = open("AOC2.txt", "r")
    for line in f:
        temp = line.split(" ")
        if temp[1] != "7":
            temp[1] = temp[1][:len(temp[1]) - 1]
        if temp[0] == "forward":
            horizontal += int(temp[1])
            vertical += int(temp[1]) * aim
        elif temp[0] == "up":
            aim -= int(temp[1])
        else:
            aim += int(temp[1])
    print(horizontal * vertical)

if __name__ == "__main__":
    main()
