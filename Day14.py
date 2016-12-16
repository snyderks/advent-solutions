# One-Time Pad Key generation
# MD5 hash the input until I see three of the same character in a row in the hash
# If one of the next 1000 contains the same character five times, hash is valid
# Need to know which index is the 64th key
import hashlib
from operator import itemgetter

base = "cuanljph"
toCheck = []
keys = []

def md5Input(index):
    m = hashlib.md5()
    m.update(bytes(base + str(index), 'utf-8'))
    return m.hexdigest()

def findRepeat(h, index):
    for i in range(0, len(h)-2):
        if h[i] is h[i+1] and h[i] is h[i+2]:
            # print("Checking " + h[i] + " at index " + str(index) + " for hash " + h)
            return (h[i], index)
    return None

def checkForChars(h, index, toCheck, keys):
    for c in toCheck:
        # somehow I was outputting things twice. No idea how.
        if c[1] + 1000 < index or c in keys:
            toCheck.remove(c)
    newCheck = []
    for c in toCheck:
        if c[0] * 5 in h:
            # print("Found " + c[0] * 5 + " (index " + str(c[1]) + ") in " + h)
            keys.append(c)
            keys.sort(key=itemgetter(1))
        else:
            newCheck.append(c)
    toCheck = newCheck

i = 0
currKeys = len(keys)
while len(keys) < 64:
    h = md5Input(i)
    repeat = findRepeat(h, i)
    if repeat is not None:
        # I was checking it against itself. Switching the order helps.
        checkForChars(h, i, toCheck, keys)
        toCheck.append(repeat)
    i += 1
print(keys[63][1])

# Part 2
def md5InputPart2(index):
    nextInput = base + str(index)
    for i in range(0, 2017):
        m = hashlib.md5()
        m.update(bytes(nextInput, 'utf-8'))
        nextInput = m.hexdigest()
    return nextInput

j = 0
keys = []
toCheck = []
while len(keys) < 100:
    h = md5InputPart2(j)
    repeat = findRepeat(h, j)
    if repeat is not None:
        # I was checking it against itself. Switching the order helps.
        checkForChars(h, j, toCheck, keys)
        toCheck.append(repeat)
    j += 1
print(keys)
print(keys[63][1])

