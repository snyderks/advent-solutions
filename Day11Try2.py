import copy
import gc
from collections import Counter

steps = 1
seen = []
done = False
# 1 = Promethium
# 2 = Cobalt
# 3 = Curium
# 4 = Ruthenium
# 5 = Plutonium
# [Elevator, generators, chips]
start = [
    [ True, [1], [1] ],
    [ False, [2, 3, 4, 5], [] ],
    [ False, [], [2, 3, 4, 5] ],
    [ False, [], [] ],
    0]

def success(state):
    correct = True
    if state[4] is not 3:
        return False
    for i in range(0,3):
        if state[i][0] is not False or len(state[i][1]) > 0 or len(state[i][2]) > 0:
            correct = False
            break
    if state[3][0] is not True or len(state[3][1]) is 0 or len(state[3][2]) is 0:
        correct = False
    return correct

def duplicate(node):
    dupe = False
    # this might have been the most important optimization.
    # when checking for duplicates, it's increasingly likely that
    # the states reached by that step are very similar to the ones
    # reached by its siblings. So...we should be checking then.
    for j in range(len(seen), 0):
        if dupe:
            break
        localDupe = True
        for i in range(0, 3):
            if (seen[j][i][0] != node[i][0] or
                set(seen[j][i][1]) != set(node[i][1]) or set(seen[j][i][2]) != set(node[i][2])):
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
        newFloors[startFloor + offset][0] = True
        newFloors[startFloor][0] = False
        newFloors[4] = startFloor + offset
    return newFloors

def moveOneChip(startNode, stFlr, offset):
    states = []
    for chip in startNode[stFlr][1]:
        new = moveIndices(startNode, stFlr, [[1, chip]], offset)
        if not duplicate(new):
            states.append(new)
    return states

def moveOneGenerator(startNode, stFlr, offset):
    states = []
    for gen in startNode[stFlr][2]:
        new = moveIndices(startNode, stFlr, [[2, gen]], offset)
        if not duplicate(new):
            states.append(new)
        else:
            seen.append(new)
    return states

def moveTwoChips(startNode, stFlr, offset):
    states = []
    for chipIndex1 in range(0, int(len(startNode[stFlr][1])/2) + 1):
        for chipIndex2 in range(chipIndex1 + 1, len(startNode[stFlr][1])):
            new = moveIndices(startNode,
                              stFlr,
                              [ [1, startNode[stFlr][1][chipIndex1]],
                                [1, startNode[stFlr][1][chipIndex2]] ],
                              offset)
            if not duplicate(new):
                states.append(new)
            else:
                seen.append(new)
    return states

def moveTwoGenerators(startNode, stFlr, offset):
    states = []
    for genIndex1 in range(0, int(len(startNode[stFlr][2])/2) + 1):
        for genIndex2 in range(genIndex1 + 1, len(startNode[stFlr][2])):
            new = moveIndices(startNode,
                              stFlr,
                              [ [2, startNode[stFlr][2][genIndex1]],
                                [2, startNode[stFlr][2][genIndex2]] ],
                              offset)
            if not duplicate(new):
                states.append(new)
            else:
                seen.append(new)
    return states

def movePairs(startNode, stFlr, offset):
    states = []
    for chip in startNode[stFlr][1]:
        if chip in startNode[stFlr][2]:
            new = moveIndices(startNode,
                              stFlr,
                              [ [1, chip], [2, chip] ],
                              offset)
            if not duplicate(new):
                states.append(new)
            else:
                seen.append(new)
    return states

def generateOneDirection(startNode, stFlr, offset):
    states = []
    if offset is 1:
        if len(startNode[stFlr][1]) > 1:
            states += moveTwoChips(startNode, stFlr, offset)
        else:
            states += moveOneChip(startNode, stFlr, offset)
        if len(startNode[stFlr][2]) > 1:
            states += moveTwoGenerators(startNode, stFlr, offset)
        else:
            states += moveOneGenerator(startNode, stFlr, offset)
    else:
        empty = True
        for i in range(stFlr, 0, -1):
            if len(startNode[i][1]) > 0 or len(startNode[i][2]) > 0:
                empty = False
                break
        if not empty:
            states += moveTwoChips(startNode, stFlr, offset)
            states += moveOneChip(startNode, stFlr, offset)
            states += moveTwoGenerators(startNode, stFlr, offset)
            states += moveOneGenerator(startNode, stFlr, offset)

    states += movePairs(startNode, stFlr, offset)
    return states

def generateBothDirections(startNode, stFlr):
    return (generateOneDirection(startNode, stFlr, 1) +
           generateOneDirection(startNode, stFlr, -1))

def generateStates(startNode, stFlr):
    states = []
    if stFlr is 3:
        states = generateOneDirection(startNode, stFlr, -1)
    elif stFlr is 0:
        states = generateOneDirection(startNode, stFlr, 1)
    else:
        states = generateBothDirections(startNode, stFlr)
    return states

def step(states):
    next_states = []
    for state in states:
        if success(state):
            done = True
            next_states = []
            break
        else:
            next_states += generateStates(state, state[4])
    return next_states

currNodes = [start]

while done is False:
    print(str(len(currNodes)))
    # print(str(len(currNodes)))
    currNodes = step(currNodes)
    steps += 1

print(steps)
