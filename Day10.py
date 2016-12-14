# Day 10: http://adventofcode.com/2016/day/10
# Problem: Bots give each other chips with numbers on them only when they have
# two of them. Determine which one is responsible for comparing two specific
# numbers.

f = open("inputs/Day10.txt")

import re
from collections import defaultdict

botSend = re.compile(r"(?:bot )(\d+)(?: gives low to (\w+) )(\d+)(?: and high to (\w+) )(\d+)")
botReceive = re.compile(r"(?:value )(\d+)(?: goes to bot )(\d+)")

values = [61, 17]

lines = f.readlines()
finishedLines = []

bots = defaultdict(list)
outs = defaultdict(list)

def checkBots(bots, values):
    for key, value in bots.items():
        if values[0] in value and values[1] in value:
            return key
    return None

# A note: if you have numbers, beware of string comparisons. They do NOT work the same.

while len(lines) > len(finishedLines):
    for line in lines:
        if line in finishedLines:
            continue
        if 'value' in line:
            [value, bot] = botReceive.search(line).groups()
            bots[bot].append(int(value))
            finishedLines.append(line)
        else:
            [bot, lowType, lowDest, highType, highDest] = botSend.search(line).groups()
            if len(bots[bot]) < 2:
                continue # need more values
            else:
                low  = min(bots[bot])
                high = max(bots[bot])
                bots[bot] = []
                if lowType.startswith('out'):
                    outs[lowDest].append(low)
                else:
                    bots[lowDest].append(low)
                if highType.startswith('out'):
                    outs[highDest].append(high)
                else:
                    bots[highDest].append(high)
                finishedLines.append(line)
        check = checkBots(bots, values)
        if check is not None:
            print(check)

# Part 2: Multiply the values of one chip in outputs 0, 1, 2
print(str(outs['0'][0] * outs['1'][0] * outs['2'][0]))