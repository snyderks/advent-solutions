from collections import defaultdict
import copy

registers = defaultdict(int)
registers['a'] = 0
registers['b'] = 0
registers['c'] = 1
registers['d'] = 0

f = open('inputs/Day12.txt')

lines = f.read().splitlines()

def copy(r1, r2):
    if r1.isdigit():
        registers[r2] = int(r1)
    else:
        registers[r2] = registers[r1]

def inc(r1):
    registers[r1] += 1

def dec(r1):
    registers[r1] -= 1

def jnz(currLine, r1, offset):
    if r1.isdigit():
        if int(r1) != 0:
            return currLine + int(offset)
        else:
            return currLine + 1
    elif registers[r1] != 0:
        return currLine + int(offset)
    else:
        return currLine + 1

i = 0

while i < len(lines):
    args = lines[i].split(" ")
    if "cpy" in lines[i]:
        copy(args[1], args[2])
    elif "inc" in lines[i]:
        inc(args[1])
    elif "dec" in lines[i]:
        dec(args[1])
    elif "jnz" in lines[i]:
        i = jnz(i, args[1], args[2]) - 1
    i += 1

print(registers['a'])
