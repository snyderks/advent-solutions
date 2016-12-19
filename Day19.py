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

# Part 2 is a modified Josephus.