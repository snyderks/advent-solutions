import copy

steps = 1
seen = []
# 1 = Promethium
# 2 = Cobalt
# 3 = Curium
# 4 = Ruthenium
# 5 = Plutonium
# [Elevator, generators, chips]
start = [True, [1], [1],
         False, [2, 3, 4, 5], [],
         False, [], [2, 3, 4, 5],
         False, [], []]

def success(state):
    correct = True
    for i in range(0,3):
        if state[i][0] is not False or len(state[i][1]) > 0 or len(state[i][2]) > 0:
            correct = False
            break
    if state[3][0] is not True or len(state[3][1]) is 0 or len(state[3][2]) is 0:
        correct = False
    return correct

def duplicate(node):
    dupe = False
    for state in seen:
        if dupe:
            break
        localDupe = True
        for i, floor in enumerate(state):
            if floor[0] != node[i][0] or set(floor[1]) != set(node[i][1]) or set(floor[2]) != set(node[i][2]):
                localDupe = False
                break
        if localDupe:
            dupe = True
            break

def moveIndices(floors, startFloor, indices, offset):
    # indicies are in form group (either the generators (1) or chips (2)) and the item to move
    newFloors = copy.deepcopy(floors)
    for item in indices:
        newFloors[startFloor + offset][item[0]].append(item[1])
        newFloors[startFloor][item[0]].remove(item[1])
    return newFloors

def generateStates(startNode, stFlr):
    if stFlr % 3 is not 0:
        if len(startNode[stFlr][1]) is 1 and len(startNode[stFlr][2]) is 1:
            new = moveIndices(startNode, stFlr, [[1, startNode[stFlr][1][0]], [2, startNode[stFlr][2][0]]], 1)
    
