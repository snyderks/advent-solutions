# Day 1: http://adventofcode.com/2016/day/1
# Problem: 
# given the following directions, determine how many blocks (using taxicab coordinates)
# away you are. This means that the total amount moved in x and y summed is the answer.
# The directions are in turns, so I kept track of the current direction, turned, and then
# moved by adding to or subtracting the current relational coordinates.

# pylint: disable-msg=C0103
# pylint: disable-msg=C0301

directionStr = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"

directions = directionStr.split(", ")

coords = [0, 0] # x, y

currentDirection = 1 # UP, 2 is R, 3 is D, 4 is L

def changeDirection(start, direction):
    if "L" in direction:
        if start == 1:
            start = 4
        else:
            start -= 1
    elif "R" in direction:
        if start == 4:
            start = 1
        else:
            start += 1
    elif "D" in direction:
        if start < 3:
            start += 2
        else:
            start -= 2
    return start


def move(directionNum, magnitude, coords):
    if directionNum == 1:
        coords[1] += int(magnitude[1:])
    if directionNum == 2:
        coords[0] += int(magnitude[1:])
    if directionNum == 3:
        coords[1] -= int(magnitude[1:])
    if directionNum == 4:
        coords[1] -= int(magnitude[1:])
    return coords

for direction in directions:
    currentDirection = changeDirection(currentDirection, direction)
    coords = move(currentDirection, direction, coords)

print("Destination is " + str(coords[0] + coords[1]) + " blocks away\n")