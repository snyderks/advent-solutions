# Day 11: http://adventofcode.com/2016/day/11
# Problem: Really need to read the page, but essentially it's a
# river crossing problem. Breadth-first search is the way to go here.

from collections import defaultdict
import copy

currentLevel = 0

class Level:
    def __init__(self, nodes = [], currentLevel = 0):
        self.nodes = nodes
        self.levelNumber = currentLevel + 1

class Floor:
    def __init__(self, number, lift=False, chips=[], generators=[]):
        self.lift = lift
        self.chips = chips
        self.generators = generators

class Floors:
    def __init__(self, floors, parent, elFloor):
        self.parent = parent
        self.floors = floors
        self.elFloor = elFloor
    def checkFloors(self):
        # check all floors to make sure no chips are alone with
        # generators on the same floor
        for floor in self.floors:
            for generator in floor.generators:
                if generator not in floor.chips and len(floor.generators) > len(floor.chips) and len(floor.chips) > 0:
                    return False
        return True
    def finished(self):
        correct = True
        for i, floor in enumerate(self.floors):
            if i < 3 and len(floor.chips) is not 0 or len(floor.generators) is not 0 or floor.lift is True:
                correct = False
                break
        if self.floors[3].lift is False:
            correct = False
        return correct

            

levels = []

# Going to manually build the input because it's easier.

floorArr = []

floorArr.append(Floor(1, True, ['promethium'], ['promethium']))
floorArr.append(Floor(2, False, [], ['cobalt', 'curium', 'ruthenium', 'plutonium']))
floorArr.append(Floor(3, False, ['cobalt', 'curium', 'ruthenium', 'plutonium']))
floorArr.append(Floor(4))

firstFloors = Floors(floorArr, None, 0)

levels.append(Level([firstFloors], currentLevel))
currentLevel += 1

def addNodes(floors):
    newLevel = []
    floorArr = floors.floors
    downFloor = floorArr[floors.elFloor-1]
    # start by two branches: up a floor or down a floor
    if floors.elFloor > 0 and len(downFloor.generators) is not 0 and len(downFloor.chips) is not 0:
        newLevel += allPossibleMovesInOneDirection(floors, -1)
    if floors.elFloor < 3:
        newLevel += allPossibleMovesInOneDirection(floors, 1)
    # print("Next level: " + str(newLevel))
    return newLevel
        

def checkIfUnique(node):
    unique = True
    for level in levels:
        if unique is False:
            break
        for validNode in level.nodes:
            equal = True
            for i, floor in enumerate(validNode.floors):
                if floor.lift != node.floors[i].lift or set(floor.chips) != set(node.floors[i].chips) or set(floor.generators) != set(node.floors[i].generators):
                    equal = False
            if equal:
                unique = False
                break
    return unique

def allPossibleMovesInOneDirection(floors, offset):
    newFloors = []
    currentFloor = floors.floors[floors.elFloor]
    for chip in currentFloor.chips:
        # print("Entering pairs of chips and generators")
        if chip in currentFloor.generators:
            node = copy.deepcopy(floors)
            nodeFloors = node.floors
            node.parent = floors
            nodeFloors[node.elFloor + offset].chips.append(chip)
            nodeFloors[node.elFloor + offset].generators.append(chip)
            nodeFloors[node.elFloor + offset].lift = True
            nodeFloors[node.elFloor].chips.remove(chip)
            nodeFloors[node.elFloor].generators.remove(chip)
            nodeFloors[node.elFloor].lift = False
            node.elFloor = node.elFloor + offset

            if checkIfUnique(node) and node.checkFloors():
                newFloors.append(node)
            else:
                print("Not unique")
    
    for chip in currentFloor.chips:
        node = copy.deepcopy(floors)
        nodeFloors = node.floors
        node.parent = floors
        nodeFloors[node.elFloor + offset].chips.append(chip)
        nodeFloors[node.elFloor].chips.remove(chip)
        nodeFloors[node.elFloor + offset].lift = True
        nodeFloors[node.elFloor].lift = False
        node.elFloor = node.elFloor + offset

        if checkIfUnique(node) and node.checkFloors():
            newFloors.append(node)
    if len(currentFloor.chips) is 1:
        # print("Entering one chip")
        node = copy.deepcopy(floors)
        nodeFloors = node.floors
        node.parent = floors
        firstChip = nodeFloors[node.elFloor].chips[0]
        nodeFloors[node.elFloor + offset].chips.append(firstChip)
        nodeFloors[node.elFloor].chips.remove(firstChip)
        nodeFloors[node.elFloor + offset].lift = True
        nodeFloors[node.elFloor].lift = False
        node.elFloor = node.elFloor + offset

        if checkIfUnique(node) and node.checkFloors():
            newFloors.append(node)
        else:
            print("Not unique")
    else:
        for i in range(0, int(len(currentFloor.chips)/2) + 1):
            # print("Entering pairs of chips")
            for j in range(i+1, len(currentFloor.chips)):
                node = copy.deepcopy(floors)
                nodeFloors = node.floors
                node.parent = floors
                firstChip = nodeFloors[node.elFloor].chips[i]
                secondChip = nodeFloors[node.elFloor].chips[j]
                nodeFloors[node.elFloor + offset].chips.extend([firstChip, secondChip])
                nodeFloors[node.elFloor].chips.remove(firstChip)
                nodeFloors[node.elFloor].chips.remove(secondChip)
                nodeFloors[node.elFloor + offset].lift = True
                nodeFloors[node.elFloor].lift = False
                node.elFloor = node.elFloor + offset
                
                if checkIfUnique(node) and node.checkFloors():  
                    newFloors.append(node)
                else:
                    print("Not unique")

    for generator in currentFloor.generators:
        node = copy.deepcopy(floors)
        nodeFloors = node.floors
        node.parent = floors
        nodeFloors[node.elFloor + offset].generators.append(generator)
        nodeFloors[node.elFloor].generators.remove(generator)
        nodeFloors[node.elFloor + offset].lift = True
        nodeFloors[node.elFloor].lift = False
        node.elFloor = node.elFloor + offset
        
        if checkIfUnique(node) and node.checkFloors():
            newFloors.append(node)
    if len(currentFloor.generators) is 1:
        # print("Entering one generator")
        node = copy.deepcopy(floors)
        nodeFloors = node.floors
        node.parent = floors
        firstGenerator = nodeFloors[node.elFloor].generators[0]
        nodeFloors[node.elFloor + offset].generators.append(firstGenerator)
        nodeFloors[node.elFloor].generators.remove(firstGenerator)
        nodeFloors[node.elFloor + offset].lift = True
        nodeFloors[node.elFloor].lift = False
        node.elFloor = node.elFloor + offset
        
        if checkIfUnique(node) and node.checkFloors():
            newFloors.append(node)
        else:
            print("Not unique")
    else:
        for i in range(0, int(len(currentFloor.generators)/2) + 1):
            # print("Entering pairs of generators")
            for j in range(i+1, len(currentFloor.generators)):
                node = copy.deepcopy(floors)
                nodeFloors = node.floors
                node.parent = floors
                firstGenerator = nodeFloors[node.elFloor].generators[i]
                secondGenerator = nodeFloors[node.elFloor].generators[j]
                nodeFloors[node.elFloor + offset].generators.extend([firstGenerator, secondGenerator])
                nodeFloors[node.elFloor].generators.remove(firstGenerator)
                nodeFloors[node.elFloor].generators.remove(secondGenerator)
                nodeFloors[node.elFloor + offset].lift = True
                nodeFloors[node.elFloor].lift = False
                node.elFloor = node.elFloor + offset

                if checkIfUnique(node) and node.checkFloors():
                    newFloors.append(node)
                else:
                    print("Not unique")
    return newFloors

done = False

steps = 0

end = None

while done is False and len(levels[-1].nodes) > 0:
    print("Current Level: " + str(currentLevel))
    nextLevel = []
    print(str(len(levels[-1].nodes)) + " nodes in the current level")
    for floors in levels[-1].nodes:
        if floors.finished():
            steps = currentLevel
            done = True
            end = floors
            break
        if floors.checkFloors() is False:
            levels[-1].nodes.remove(floors)
        else:
            nextLevel += addNodes(floors)
    print(str(len(nextLevel)) + " nodes in the next level")
    levels.append(Level(nextLevel, currentLevel))
    currentLevel += 1
        

print(steps)

for floor in end.floors:
    print("Chips: " + str(floor.chips))
    print("Generators: " + str(floor.generators))
    print("Elevator on floor:" + str(floor.lift))

parentFloors = end.parent

while parentFloors is not None:
    for floor in parentFloors.floors:
        print("Chips: " + str(floor.chips))
        print("Generators: " + str(floor.generators))
        print("Elevator on floor:" + str(floor.lift))
    parentFloors = parentFloors.parent


