import re

driveData = re.compile("(?:x)(\d+)(?:-y)(\d+)(?:\s+)(\d+)(?:T\s+)(\d+)(?:T\s+)(\d+)")

lines = open("inputs/Day22.txt", "r").readlines()

# X, Y, Size, Used, Available
# 0, 1,  2,    3,       4
drives = map(lambda line: driveData.search(line).groups(), lines)
drives = list(map(lambda drive: list(map(int, drive)), drives))

viablePairs = 0

runs = 0

for a in drives:
    if a[3] > 0:
        for b in drives:
            if a is not b and a[3] <= b[4]:
                # print(str(a[3]) + " to "  + str(b[4]))
                viablePairs += 1

print(str(viablePairs))

# Part 2 is a path-walker but more of a push where you have to 
# clear out the path in advance.
# The priority will be given to those with the empty node closest to
# the goal data and also the goal data closest to the accessible node.

emptyDrive = []
emptyDriveKey = ""
INITGOALX = 33
INITGOALY = 0
# find the empty drive
for drive in drives:
    if drive[3] is 0:
        emptyDrive = drive
        emptyDriveKey = "x" + str(drive[0]) + "y" + str(drive[1])
        break

def findDriveWithCoords(x, y, drives):
    for drive in drives:
        if drive[0] is x and drive[1] is y:
            return "x" + str(drive[0]) + "y" + str(drive[1])
    return None

# Have to convert the drives into a grid of height 30, width 34
driveGrid = {}
for drive in drives:
    rlud = []
    if drive[0] > 0 and drive[0] < 34:
        rlud.append(findDriveWithCoords(drive[0] + 1, drive[1], drives))
        rlud.append(findDriveWithCoords(drive[0] - 1, drive[1], drives))
    elif drive[0] > 0:
        rlud.append(findDriveWithCoords(drive[0] - 1, drive[1], drives))
    elif drive[0] < 34:
        rlud.append(findDriveWithCoords(drive[0] + 1, drive[1], drives))
    if drive[1] > 0 and drive[1] < 30:
        rlud.append(findDriveWithCoords(drive[0], drive[1] - 1, drives))
        rlud.append(findDriveWithCoords(drive[0], drive[1] + 1, drives))
    elif drive[1] > 0:
        rlud.append(findDriveWithCoords(drive[0], drive[1] - 1, drives))
    elif drive[1] < 30:
        rlud.append(findDriveWithCoords(drive[0], drive[1] + 1, drives))

    # x, y, the adjacent nodes, whether it's
    # passable by the empty node, and
    # whether it's the goal drive.
    node = [drive[0], drive[1], [], drive[3] <= emptyDrive[4], drive[0] is 33 and drive[1] is 0]
    for d in rlud:
        if d is not None:
            node[2].append(d)
    driveGrid["x" + str(drive[0]) + "y" + str(drive[1])] = node

# First, make a queue.
import queue
q = queue.PriorityQueue()

seen = []

def walkToGoal(q):
    d = q.get()
    if d[0] is 1: # no dist to goal (done)
        return d
    for adjKey in d[1][2]:
        adj = driveGrid[adjKey]
        if adj[3] and adjKey not in seen: # passable
            q.put((abs(INITGOALX - adj[0])+abs(INITGOALY - adj[1]), adj, d[2] + 1))
            seen.append(adjKey)
    return None

# Now have to add the empty node.
d = driveGrid[emptyDriveKey]
q.put((abs(INITGOALX - d[0])+abs(INITGOALY - d[1]), d, 0))

adjToGoal = None
while adjToGoal is None:
    adjToGoal = walkToGoal(q)

print(adjToGoal)

seen = []

def pushToMyDrive(q):
    d = q.get()
    if d[0] is 0:
        return d
    for adjKey in d[2][2]:
        adj = driveGrid[adjKey]
        if adj[3]: # passable
            if adj[0] is d[1][0] and adj[1] is d[1][1]:
                toAdd = (d[2][0] + d[2][1], (d[2][0], d[2][1]), adj, d[3] + 1)
                if toAdd not in seen:
                    q.put(toAdd)
                    seen.append(toAdd)
            # To get it to run fast, keep the empty drive close and prune
            # all noncomplying states.
            elif abs(adj[0]-d[1][0]) + abs(adj[1]-d[1][1]) <= 2:
                toAdd = (d[0], d[1], adj, d[3] + 1)
                if toAdd not in seen:
                    q.put(toAdd)
                    seen.append(toAdd)
    return None

q = queue.PriorityQueue()
# dist of goal drive from 0, 0; goal drive coords; drive; steps
q.put((INITGOALX + INITGOALY + adjToGoal[2], (INITGOALX, INITGOALY), adjToGoal[1], adjToGoal[2]))

last = None
while last is None:
    last = pushToMyDrive(q)

print("\n" + str(last))