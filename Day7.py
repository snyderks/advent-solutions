# Day 7: http://adventofcode.com/2016/day/7
# Problem: Given "IPv7" strings in the format abcde[abcde]abcde
# (with each section being any length greater than 0), determine
# how many of them have a pair of letters followed by the reverse pair
# (e.x. abba) outside the brackets but also not inside them.

import re

# selects the group inside the brackets
brackRegex = re.compile("(?:\[)([a-zA-Z]+)(?:])")
# selects portion outside brackets
outBrackRegex = re.compile("(?:\]|^)(\w+)(?:\[|$)")

f = open("inputs/Day7.txt", "r")
valid = 0

for line in f:
    invalid = False
    brackets = brackRegex.findall(line)
    for group in brackets:
        if len(group) > 3 and not invalid:
            for i in range(3, len(group)):
                if (group[i] is group[i-3] and
                        group[i-1] is group[i-2] and
                        group[i] is not group[i-1]):
                    invalid = True
                    break
        else:
            break

    if not invalid:
        outBrackets = outBrackRegex.findall(line)
        # Proved it's not invalid. Now prove it is valid.
        invalid = True
        for group in outBrackets:
            if len(group) > 3 and invalid:
                for i in range(3, len(group)):
                    if (group[i] is group[i-3] and
                            group[i-1] is group[i-2] and
                            group[i] is not group[i-1]):
                        invalid = False
                        break
            else:
                break

    if not invalid:
        valid += 1

print("IPs with TLS: " + str(valid))

# Part 2:
# Determine how many IPs support Super Secret Listening (SSL).
# If it supports it, it has a set of three characters, two outside being the same,
# one inside different (like aba) in the outside section replicated in one of the
# bracketed sections, but reversed in position (like bab).

withSSL = 0

f = open("inputs/Day7.txt", "r")

for line in f:
    hasSSL = False
    brackets = brackRegex.findall(line)
    outBrackets = outBrackRegex.findall(line)
    for group in brackets:
        if len(group) > 2:
            for i in range(2, len(group)):
                if group[i] is group[i-2] and group[i] is not group[i-1]:
                    # Area-Broadcast Accessor (three letters in the brackets reversed)
                    searchABA = "".join(group[i-1] + group[i] + group[i-1])
                    # Remember to change iterator variable in nested loops.
                    for outGroup in outBrackets:
                        if searchABA in outGroup:
                            hasSSL = True
                            break
                if hasSSL:
                    break
        if hasSSL:
            break
    if hasSSL:
        withSSL += 1

print("IPs with SSL: " + str(withSSL))
