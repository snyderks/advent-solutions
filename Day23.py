from collections import defaultdict

lines = open("inputs/Day23.txt", "r").read().splitlines()
# Adding a bool to toggle by tgl
lines = list(map(lambda line: [line, False], lines))

registers = defaultdict(int)
registers['a'] = 7
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0

def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        pass
    return False

def tgl(currLine, r1):
    r = (int(r1) if r1.isdigit() else int(registers[r1])) + currLine
    if r >= 0 and r < len(lines):
        lines[r][1] = not lines[r][1]

def cpy(r1, r2):
    if isNumber(r1):
        registers[r2] = int(r1)
    else:
        registers[r2] = registers[r1]

def inc(r1):
    registers[r1] += 1

def dec(r1):
    registers[r1] -= 1

def jnz(currLine, r1, offset):
    if isNumber(r1):
        if int(r1) != 0:
            if isNumber(offset):
                return currLine + int(offset)
            elif offset in registers:
                return currLine + int(registers[offset])
            else:
                return currLine + 1
        else:
            return currLine + 1
    elif registers[r1] is not 0:
        if isNumber(offset):
            return currLine + int(offset)
        elif offset in registers:
            return currLine + int(registers[offset])
        else:
            return currLine + 1
    else:
        return currLine + 1

i = 0

while i < len(lines):
    line = lines[i][0]
    toggled = lines[i][1]
    args = line.split(" ")
    # print(str(registers) + " i: " + str(i))
    # print(line + " " + str(toggled))
    if toggled:
        if len(args) is 2:
            if "inc" in line:
                dec(args[1])
            elif not args[1].isdigit(): # can't execute inc 1, for example
                inc(args[1])
        else:
            if "jnz" in line and not args[2].isdigit(): # can't copy 1 to 2
                cpy(args[1], args[2])
            else:
                i = jnz(i, args[1], args[2]) - 1
    else:
        if "cpy" in line:
            cpy(args[1], args[2])
        elif "inc" in line:
            inc(args[1])
        elif "dec" in line:
            dec(args[1])
        elif "jnz" in line:
            i = jnz(i, args[1], args[2]) - 1
        elif "tgl" in line:
            tgl(i, args[1])
    i += 1

print("a is " + str(registers['a']))

# Part 2: regA is now 12. Apparently it's supposed to take too long, so I need to
# figure out if I can multiply.
# What I did: I wrote my own instructions and rewrote the assembunny code to
# speed it up. I could do something like JIT compilation, but...eh.

def amult(r1, r2, r3):
    if not isNumber(r3):
        r1 = int(r1) if isNumber(r1) else int(registers[r1])
        r2 = int(r2) if isNumber(r2) else int(registers[r2])
        registers[r3] += r1 * r2

def add(r1, r2):
    if not isNumber(r2):
        r1 = int(r1) if isNumber(r1) else int(registers[r1])
        registers[r2] += r1

lines = open("inputs/Day23MODIFIED.txt", "r").read().splitlines()
# Adding a bool to toggle by tgl
lines = list(map(lambda line: [line, False], lines))

registers = defaultdict(int)
registers['a'] = 12
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0

i = 0

while i < len(lines):
    line = lines[i][0]
    toggled = lines[i][1]
    args = line.split(" ")
    # print(str(registers) + " i: " + str(i))
    # print(line + " " + str(toggled))
    if toggled:
        if len(args) is 2:
            if "inc" in line:
                dec(args[1])
            elif not args[1].isdigit(): # can't execute inc 1, for example
                inc(args[1])
        else:
            if "jnz" in line and not args[2].isdigit(): # can't copy 1 to 2
                cpy(args[1], args[2])
            else:
                i = jnz(i, args[1], args[2]) - 1
    else:
        if "cpy" in line:
            cpy(args[1], args[2])
        elif "inc" in line:
            inc(args[1])
        elif "dec" in line:
            dec(args[1])
        elif "jnz" in line:
            i = jnz(i, args[1], args[2]) - 1
        elif "tgl" in line:
            tgl(i, args[1])
        elif "amult" in line:
            amult(args[1], args[2], args[3])
        elif "add" in line:
            add(args[1], args[2])
    i += 1
    # input()

print("a is " + str(registers['a']))