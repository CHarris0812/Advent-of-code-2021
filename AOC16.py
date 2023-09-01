version = 0

def part1():
    global version
    hex = hexadecimalDict()
    data = "EE00D40C823060"
    binaryString = hexToBin(data, hex)
    decodePacket(binaryString)
    return version

def decodePacket(binaryString):
    global version
    if binaryString.count("1") == 0:
        binaryString = ""
    while(len(binaryString) > 0):
        temp = binaryString[:3]
        binaryString = binaryString[3:]
        ver = int(temp, 2)
        print(ver)
        version += ver

        temp = binaryString[:3]
        binaryString = binaryString[3:]
        id = int(temp, 2)
        if id == 4:
            binaryString, value = literal(binaryString)
        else:
            temp = binaryString[:1]
            binaryString = binaryString[1:]
            lenId = 15 if temp == "0" else 11

            temp = binaryString[:lenId]
            binaryString = binaryString[lenId:]
            size = int(temp, 2)

            temp = binaryString[:size]
            binaryString = binaryString[size:]
            packets = temp
            decodePacket(packets)
        if binaryString.count("1") == 0:
            binaryString = ""

def literal(binaryString):
    found = False
    val = ""
    while not found:
        temp = binaryString[:5]
        binaryString = binaryString[5:]
        if temp[0] == "0":
            found = True
        val += temp[1:]
    return binaryString, val

def hexadecimalDict():
    return {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def hexToBin(data, hex):
    binaryString = ""
    for i in data:
        binaryString += hex[i]
    return binaryString

if __name__ == "__main__":
    print(part1())
    #print(part2())
