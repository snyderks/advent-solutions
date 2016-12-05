# Day 3: http://adventofcode.com/2016/day/3
# Problem: Given lists of the length of sides of triangles, determine how many
# of the given triangles are possible.

import re

originalTriangles = open("inputs/Day3.txt").read().split("\n")

pattern = re.compile("(?:\s*)(\d+)(?:\s+)(\d+)(?:\s+)(\d+)")

for i, val in enumerate(originalTriangles):
    if val.isspace() or len(val) == 0:
        originalTriangles.pop(i)

def createSides(str):
    groups = pattern.search(str).groups()
    nums = []
    for group in groups:
        nums.append(int(group))
    return nums

triangles = map(createSides, originalTriangles)

correct = 0

for triangle in triangles:
    valid = True
    for number in triangle:
        if sum(triangle) - number <= number: # Less than or equal to! Line != triangle
            valid = False
            break
    if valid == True:
        correct += 1

print(correct)

# Part 2: Attempt to read by column. Each group of three in a column is now a triangle.
# How many of those triangles are valid?

triangles = []
correct = 0

for i in range(2, len(originalTriangles), 3):
    triangleSet = [[], [], []]
    for j in range(i-2, i+1):
        groups = pattern.search(originalTriangles[j]).groups()
        for index, group in enumerate(groups):
            triangleSet[index].append(int(group))
    triangles.extend(triangleSet)

for triangle in triangles:
    valid = True
    for number in triangle:
        if sum(triangle) - number <= number: # Less than or equal to! Line != triangle
            valid = False
            break
    if valid == True:
        correct += 1

print(correct)