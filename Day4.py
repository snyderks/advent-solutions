#!/usr/local/bin/python3

# Day 2: http://adventofcode.com/2016/day/3
# Problem: Given lists of the length of sides of triangles, determine how many
# of the given triangles are possible.

import re
import operator
from collections import Counter
from collections import defaultdict

letters = re.compile("(\w+(?=\-))")
digits = re.compile("(\d+)")
checksum = re.compile("(\w+(?=\]))")

def isValid(str):
    letterGroups = letters.findall(str)
    letterCounts = defaultdict(lambda: 0)
    for group in letterGroups:
        counts = Counter(group)
        for k, v in counts.items():
            letterCounts[k] += v
    # first sort alphabetically, then by value. stable sort preserves alphabetic
    # order for equals.
    # have to reverse the alphabetic order because we reverse later.
    sortedCounts = sorted(letterCounts.items(), key=operator.itemgetter(0))
    sortedCounts.reverse()
    sortedCounts = sorted(sortedCounts, key=operator.itemgetter(1))
    sortedCounts.reverse()
    check = checksum.search(str)
    valid = True
    for index, count in enumerate(sortedCounts):
        if len(check.group(0)) == index:
            break
        if check.group(0)[index] != count[0]:
            valid = False
            break
    return valid

f = open("inputs/Day4.txt", "r")
totalValidDigits = 0

for line in f:
    if isValid(line):
        totalValidDigits += int(digits.search(line).group(0))

print(totalValidDigits)
