# Day 9: http://adventofcode.com/2016/day/10
# Problem: Bots give each other chips with numbers on them only when they have
# two of them. Determine which one is responsible for comparing two specific
# numbers.

f = open("inputs/Day10.txt", "r")

import re

botSend = re.compile("(?:bot )(\d+)(?: gives low to (bot|output) )(\d+)(?: and high to (bot|output) )(\d+)")
botReceive = re.compile("(?:value )(\d+)(?: goes to bot )(\d+)")

values = [61, 17]

compBot = ""

bots = {}
for line in f:
    print(line)
    if line.isspace():
        break
    if "value" in line:
        groups = botReceive.search(line).groups()
        value = int(groups[0])
        bot = groups[1]
        if bot in bots and bots[bot]['start'] is not None:
            bots[bot].append(value)
        else:
            bots[bot]['start'] = [value]
    else:
        groups = botSend.search(line).groups()
        bot = bots[groups[0]]
        if "bot" in groups[1]:
            dest = groups[2]
            if dest in bots and len(bots[dest]) > 0:
                bots[dest].append(lo)
            else:
                bots[dest] = [lo]
        if "bot" in groups[3]:
            dest = groups[4]
            if dest in bots and len(bots[dest]) > 0:
                bots[dest].append(hi)
            else:
                bots[dest] = [hi]
        bot = []
    for key, value in bots.iteritems():
        if values[0] in value and values[1] in value:
            compBot = key
            break
    print(bots)
print(compBot)
