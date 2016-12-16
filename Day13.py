import queue
from collections import Counter
import math

goal = (31, 39)
src = 1358
q = queue.PriorityQueue()
done = False
visited = []
stepsList = []
reached = []

def calculatePriority(item):
    return int(math.sqrt(math.pow(item[0]-1, 2) + math.pow(item[1] - 1, 2))) * -1

def valid(item):
    for chk in visited:
        if chk[0][0] == item[0][0] and chk[0][1] == item[0][1] and chk[1] <= item[1]:
            return False
    return True

def isWall(item):
    if item[0] < 0 or item[1] < 0:
        return True
    x = item[0]
    y = item[1]
    bits = bin(x*x + 3*x + 2*x*y + y + y*y + src)
    counts = Counter(bits)
    if counts["1"] % 2 is 0:
        return False
    else: return True

def step():
    item = q.get()
    coords = item[1]
    if coords[0] is 31 and coords[1] is 39:
        stepsList.append(item[2])
    items = []
    items.append((coords[0], coords[1] + 1))
    items.append((coords[0], coords[1] - 1))
    items.append((coords[0] - 1, coords[1]))
    items.append((coords[0] + 1, coords[1]))

    for i in items:
        if (not isWall(i)) and valid((i, item[2] + 1)):
            q.put((calculatePriority(i), i, item[2] + 1))
            visited.append((i, item[2] + 1))

q.put((calculatePriority((1,1)), (1,1), 0))
steps = 0
while len(list(q.queue)) > 0:
    step()

print(stepsList)

# Part 2

q = queue.PriorityQueue()
visited = []

def stepToFifty():
    item = q.get()
    coords = item[1]
    if item[2] <= 50:
        reached.append(coords)
    items = []
    items.append((coords[0], coords[1] + 1))
    items.append((coords[0], coords[1] - 1))
    items.append((coords[0] - 1, coords[1]))
    items.append((coords[0] + 1, coords[1]))

    for i in items:
        if (not isWall(i)) and valid((i, item[2] + 1)):
            q.put((calculatePriority(i), i, item[2] + 1))
            visited.append((i, item[2] + 1))

q.put((calculatePriority((1,1)), (1,1), 0))
while len(list(q.queue)) > 0:
    stepToFifty()

print(len(set(reached)))
