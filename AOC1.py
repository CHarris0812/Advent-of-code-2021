def main():
    f = open('AOC1.txt','r')
    result = 0
    temp = 0
    oneBack = 0
    twoBack = 0
    prev = 0
    for line in f:
        val = int(line) + oneBack + twoBack
        if temp > 1:
            if val > prev:
                result += 1
        prev = val
        twoBack = oneBack
        oneBack = int(line)
        temp += 1
    print(result - 1)

if __name__ == "__main__":
    main()