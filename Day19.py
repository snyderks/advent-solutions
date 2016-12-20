# Classic Josephus problem (https://en.wikipedia.org/wiki/Josephus_problem)

def maxPow2(n):
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n >> 1

def getSafe(n):
    return 2 * (n - maxPow2(n)) + 1

print(str(getSafe(3004953)))

# Part 2 is a modified Josephus. Kill the opposite one (the middle)
# Ended up figuring out that midway between powers of three, it stops
# counting up by one and counts up by two. This finds the largest power
# of three and figures out whether to just count up by 1 or add a few
# 2s to then get the surviving number. Should work in O(1) with O(n)
# to find the power of three

from collections import deque
import itertools

def largestMagnitude(n):
    i = 0
    while i < n:
        if pow(3, i + 1) > n:
            return i
        else:
            i += 1
i = 3004953
power = largestMagnitude(i)
remaining = i - pow(3, power)
breakNum = int((pow(3, power + 1) - pow(3, power) + 1) / 2) + pow(3, power)
if remaining is 0:
    print(str(i) + ": " + str(i))
elif i > breakNum:
    print(str(i) + ": " + str((i - breakNum) * 2 + (breakNum - pow(3, power))))
else:
    print(str(i) + ": " + str(remaining))


# for i in range(1, 30):
    # elves = deque()
    # for j in range(1, i+1):
    #     elves.append(j)
    # while len(elves) > 1:
    #     elves.remove(list(itertools.islice(elves, 1, len(elves)))[int((len(elves)-2)/2)])
    #     elves.rotate(-1)