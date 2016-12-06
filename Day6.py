# Day 6: http://adventofcode.com/2016/day/6
# Problem: Given many lines of the same length, determine the message
# by finding the most frequent letter in each column.

from collections import Counter

f = open("inputs/Day6.txt", "r")

columns = []

for line in f:
    if len(columns) is 0:
        for char in line:
            if char is not '\n':
                columns.append([char])
    else:
        for index, char in enumerate(line):
            if char is not '\n':
                columns[index].append(char)

def mostCommonLetter(chars):
    counts = Counter(chars)
    return counts.most_common(1)[0][0]

mostCommon = map(mostCommonLetter, columns)

print("".join(mostCommon))

# Part 2:
# Get the least common letter now!

def leastCommonLetter(chars):
    counts = Counter(chars)
    return counts.most_common()[-1][0]

leastCommon = map(leastCommonLetter, columns)

print("".join(leastCommon))