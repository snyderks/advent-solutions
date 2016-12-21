from collections import deque
import re

def swapPosition(els, x, y):
    temp = els[x]
    els[x] = els[y]
    els[y] = temp
    return els

def swapLetters(els, x, y):
    for i, el in enumerate(els):
        if el is x:
            els[i] = y
        elif el is y:
            els[i] = x
    return els

def rotateAmt(els, nRight):
    els.rotate(nRight)
    return els

def rotateBasedOnLetter(els, x):
    i = els.index(x)
    if i > 3:
        i += 1
    i += 1
    return rotateAmt(els, i)

def reverseEls(els, x, y):
    els = list(els)
    toReverse = els[x:y+1]
    toReverse.reverse()
    if y+1 is len(els):
        return deque(els[:x] + toReverse)
    else:
        return deque(els[:x] + toReverse + els[y+1:])

def movePos(els, x, y):
    toMove = els[x]
    els.remove(toMove)
    els.insert(y, toMove)
    return els

digit = re.compile("(\d+)")
letter = re.compile("(?:letter )(\w+)")

# Part 1

f = open("inputs/Day21.txt")

start = deque("abcdefgh")

for line in f:
    print("".join(list(start)))
    print(line)
    if "swap" in line:
        if "position" in line:
            x, y = digit.findall(line)
            start = swapPosition(start, int(x), int(y))
        elif "letter" in line:
            x, y = letter.findall(line)
            start = swapLetters(start, x, y)
    elif "rotate" in line:
        if "step" in line:
            x = int(digit.findall(line)[0])
            if "left" in line:
                x = -x
            start = rotateAmt(start, x)
        elif "position" in line:
            x = letter.findall(line)[0]
            start = rotateBasedOnLetter(start, x)
    elif "reverse" in line:
        x, y = digit.findall(line)
        start = reverseEls(start, int(x), int(y))
    elif "move" in line:
        x, y = digit.findall(line)
        start = movePos(start, int(x), int(y))

print("".join(list(start)))
    

# Part 2
# The reversal works for strings of length 8.
# Honestly, a bit of an annoying thing since it doesn't work
# for the example.

revSteps = open("inputs/Day21.txt", "r").readlines()
revSteps.reverse()

def rotateBasedOnLetterReverse(els, x):
    i = els.index(x)
    if i is 0:
        i = -9
    elif i % 2 is 0:
        i = -5 - int(i / 2)
    else:
        i = int((i - 1) / 2) * -1 - 1
    return rotateAmt(els, i)

scrambled = deque("fbgdceah")

for line in revSteps:
    print("".join(list(scrambled)))
    print(line)
    if "swap" in line:
        if "position" in line:
            x, y = digit.findall(line)
            scrambled = swapPosition(scrambled, int(x), int(y))
        elif "letter" in line:
            x, y = letter.findall(line)
            scrambled = swapLetters(scrambled, y, x)
    elif "rotate" in line:
        if "step" in line:
            x = int(digit.findall(line)[0])
            if "right" in line:
                x = -x
            scrambled = rotateAmt(scrambled, x)
        elif "position" in line:
            x = letter.findall(line)[0]
            scrambled = rotateBasedOnLetterReverse(scrambled, x)
    elif "reverse" in line:
        x, y = digit.findall(line)
        scrambled = reverseEls(scrambled, int(x), int(y))
    elif "move" in line:
        x, y = digit.findall(line)
        scrambled = movePos(scrambled, int(y), int(x))

print("".join(list(scrambled)))