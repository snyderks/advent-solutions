# Day 9: http://adventofcode.com/2016/day/9
# Problem: Given a sequence of characters with repeat markers denoted by
# parentheses, such as (10x2) -- repeat the next 10 characters twice.
# If another repeat sequence is included in a previous one, it is not counted.
import time
import re

start = time.time()

f = open("inputs/Day9.txt", "r")

repeat = re.compile("(?:\()(\d+)(?:x)(\d+)(?:\))")

letters = f.readline()
decompressed = ""

while len(letters) > 0:
    match = repeat.search(letters)
    if match is not None:
        if match.start(0) > 0:
            decompressed += letters[:match.start(0)]
        amt = int(match.group(1))
        times = int(match.group(2))
        endIndex = match.end(0)
        if endIndex + amt < len(letters):
            decompressed += (letters[endIndex: endIndex + amt] * times)
            letters = letters[endIndex + amt:]
        else:
            decompressed += (letters[endIndex:] * times)
            letters = ""
    else:
        decompressed += letters
        letters = ""

decompressed = decompressed.strip()
print("Decompressed to: " + str(len(decompressed)) + " characters")

# Part 2: Decompress with everything. EVERYTHING. ALL THE EXPAND MARKERS
# Note: the below isn't really mine. Couldn't get the answer so I had to look
# up hints.
f = open("inputs/Day9.txt", "r")
letters = f.readline().strip()
decompressedLength = 0

def decompress(s):
    if "(" not in s:
        return len(s)
    chars = 0
    while "(" in s:
        chars += s.find("(")
        s = s[s.find("("):]
        marker = s[1:s.find(")")].split("x")
        s = s[s.find(")") + 1:]
        chars += decompress(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    chars += len(s)
    return chars

print("Length: " + str(decompress(letters)))
