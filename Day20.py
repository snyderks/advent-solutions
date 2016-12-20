from operator import methodcaller
from itertools import chain

f = open("inputs/Day20.txt", "r").readlines()

ranges = list(map(methodcaller("split", "-"), f))
ranges = list(map(lambda i: (int(i[0]), int(i[1])), ranges))
ranges.sort()

flatten = chain.from_iterable
LEFT, RIGHT = 1, -1

def mergeRanges(ranges):
    ranges = sorted(flatten(((start, LEFT), (stop, RIGHT)) for start, stop in ranges))
    c = 0
    # With all of the start and endpoints separated and marked as such,
    # walk them, adding 1 to c for a start and adding -1 for an end.
    # The first time we hit 0, it's the start. The second time, it's the end.
    for value, move in ranges:
        if c == 0:
            x = value
        c += move
        if c == 0:
            yield x, value

ranges = list(mergeRanges(ranges))

free = 0
done = False
for r in ranges:
    lo = r[0]
    hi = r[1]
    # print(str(lo))
    # print(str(free))
    # print(str(lo - free))
    if lo - free > 0:
        print(str(free))
        done = True
        break
    else:
        free = hi + 1
    # print("")
if not done:
    print(str(free))

# Part 2: How many are allowed?
# A note: I got the right answer but this doesn't account for
# max int (4294967295) not being blacklisted.
allowed = 0
for i in range(0, len(ranges)-1):
    currHi = ranges[i][1]
    nextLo = ranges[i+1][0]
    allowed += nextLo - currHi - 1
    # print("")

print(str(allowed))