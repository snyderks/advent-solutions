# Day 11: http://adventofcode.com/2016/day/11
# Problem: Bots give each other chips with numbers on them only when they have
# two of them. Determine which one is responsible for comparing two specific
# numbers.

from collections import defaultdict

currentDepth = 1

class Floors:
    __init__(self, floors, parentNode):
        self.floors = floors
        self.parentNode = parentNode

class Floor:
    __init__(self, liftPresent, chips, generators):
        self.liftPresent = liftPresent
        self.chips = chips
        self.generators = generators

class Level:
    __init__(self, levelNumber, floors):
        self.levelNumber = levelNumber
        self.floors = floors
        currentDepth += 1

levels = defaultDict(Level(currentDepth, floors))

# create the first level with the start state
levels.append(Level(currentDepth,
                    Floors([Floor(true, ['promethium'], ['promethium']),
                            Floor(false, [], ['cobalt', 'curium', 'ruthenium', 'plutonium']),
                            Floor(false, ['cobalt', 'curium', 'ruthenium', 'plutonium']),
                            Floor(false, [], [])
                           ]),
                    None))

def checkState(floors)
    for floor in floors:
        for chip in floor.chips:
            if chip not in floor.generators:
                return False
    

def search:
