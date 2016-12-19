import queue
from hashlib import md5

inputCode = "njfxhljp"
openChars = "bcdef"
directions = "UDLR"
directionsX = (0, 0, -1, 1)
directionsY = (-1, 1, 0, 0)
hashes = []
paths = []

def getHash(s):
    for h in hashes:
        if s is h[0]:
            return h[1]
    m = md5()
    m.update(bytes(s, 'UTF-8'))
    doors = m.hexdigest()[:4] # Up, Down, Left, Right
    hashes.append((s, doors))
    return doors

def getDoors(steps):
    doorStatus = getHash(inputCode + steps)
    doorsUnlocked = [] # Up, Down, Left, Right
    for c in doorStatus:
        unlocked = False
        for check in openChars:
            if check is c:
                unlocked = True
                break
        doorsUnlocked.append(unlocked)
    return doorsUnlocked

def step(q):
    loc = q.get()
    # print(loc)
    if loc[2][0] is 4 and loc[2][1] is 4:
        return loc[1]
    doors = getDoors(loc[1])
    for i, door in enumerate(doors):
        coords = (loc[2][0] + directionsX[i], loc[2][1] + directionsY[i])
        # print("Coords for moving " + directions[i] + ": " + str(coords))
        if door is True and coords[0] > 0 and coords[0] < 5 and coords[1] > 0 and coords[1] < 5:
            # print("Moving " + directions[i])
            # distX + distY, steps, coords
            q.put( ((4 - coords[0]) + (4 - coords[1]), loc[1]+directions[i], coords) )
    return None

# Part 1

part1Queue = queue.PriorityQueue()
# start with 1, 1
part1Queue.put((6, "", (1, 1)))

while True and len(list(part1Queue.queue)) > 0:
    correctSteps = step(part1Queue)
    if correctSteps is not None:
        print(correctSteps)
        break

print("done with part 1")

# Part 2: find the longest path for the password
inputs = ["njfxhljp"]

def stepPt2(q, inputCode, currentMax):
    loc = q.get()
    # print(loc)
    if loc[2][0] is 4 and loc[2][1] is 4:
        if len(loc[1]) > currentMax:
            currentMax = len(loc[1])
        return currentMax
    doors = getDoorsPt2(inputCode, loc[1])
    for i, door in enumerate(doors):
        coords = (loc[2][0] + directionsX[i], loc[2][1] + directionsY[i])
        # print("Coords for moving " + directions[i] + ": " + str(coords))
        if door is True and coords[0] > 0 and coords[0] < 5 and coords[1] > 0 and coords[1] < 5:
            # print("Moving " + directions[i])
            # distX + distY, steps, coords
            q.put( (len(loc[1]+directions[i]), loc[1]+directions[i], coords) )
    return currentMax

def getDoorsPt2(inputCode, steps):
    doorStatus = getHash(inputCode + steps)
    doorsUnlocked = [] # Up, Down, Left, Right
    for c in doorStatus:
        unlocked = False
        for check in openChars:
            if check is c:
                unlocked = True
                break
        doorsUnlocked.append(unlocked)
    return doorsUnlocked

for s in inputs:
    currentMax = 0
    part2Queue = queue.PriorityQueue()
    # start with 1, 1
    part2Queue.put((6, "", (1, 1)))
    while True and len(list(part2Queue.queue)) > 0:
        currentMax = stepPt2(part2Queue, s, currentMax)
    print("Done! " + str(currentMax))