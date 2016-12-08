# Day 8: http://adventofcode.com/2016/day/8
# Problem: With a 50 pixel wide and 6 pixel tall screen,
# how many would be lit up given the instruction input?
# The instructions can be: 
# 
# rect AxB, which is a rectangle
# of pixels starting in the top left corner A wide and B tall.
#
# rotate column x=A by B moves the column A down B pixels. Anything
# that would have fallen off the bottom wraps around to the top.
#
# rotate row y=A by B moves the row A right B pixels. Wraparound
# functions in the same manner.

from collections import deque
import re

display = [[" "] * 50] * 6

f = open("inputs/Day8.txt", "r")

def rect(width, height, display):
    for i in range(0, height):
        for j in range(0, width):
            display[i][j] = "#"
    return display

def rotateRow(row, shift, display):
    items = deque(display[row])
    items.rotate(shift)
    display[row] = list(items)
    return display

def rotateColumn(column, shift, display):
    items = deque([row[column] for row in display])
    items.rotate(shift)
    for index, row in enumerate(display):
        display[index][column] = items[index]
    return display

rectMatch = re.compile("(\d+)(?:x)(\d+)")
rotateMatch = re.compile("(?:(?:y|x)=)(\d+)(?:\s+by\s+)(\d+)")

for line in f:
    if "rect" in line:
        groups = rectMatch.search(line).groups()
        display = rect(int(groups[0]), int(groups[1]), display)
    elif "row" in line:
        groups = rotateMatch.search(line).groups()
        display = rotateRow(int(groups[0]), int(groups[1]), display)
    elif "column" in line:
        groups = rotateMatch.search(line).groups()
        display = rotateColumn(int(groups[0]), int(groups[1]), display)

litPixels = 0
for row in display:
    litPixels += row.count("#")

print("Lit pixels: " + str(litPixels))

# Part 2: What is the screen trying to display?
# Just printing it. I'm faster!

for row in display:
    print("".join(row))