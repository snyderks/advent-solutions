import copy

def swap(char):
    if char is "1":
        return "0"
    else:
        return "1"

def dragon(data, length):
    a = data
    while len(a) < length:
        b = a
        b = b[::-1]
        b = "".join(map(lambda c: swap(c), b))
        a = a + "0" + b
    return a

def check(data):
    result = ""
    for i in range(0, len(data)-1, 2):
        if data[i] is data[i+1]:
            result += "1"
        else:
            result += "0"
    return result

def checksum(data):
    result = check(data)
    while len(result) % 2 is not 1:
        result = check(result)
    return result

data = "01111010110010011"
length = 35651584

data = dragon(data, length)[:length+1]
print(checksum(data))
