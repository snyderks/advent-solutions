# Day 5: http://adventofcode.com/2016/day/5
# Problem: Using the input string, MD5 hash an increasing index (beginning at 0)
# concatenated to the input until the hex encoding of the string has 5 zeroes.
# The next character (not the next hex number, but just the next character) is
# added to the password. Continue up to eight characters.

import hashlib

input = "cxdnnyjw"
index = 0
password = ""
while len(password) < 8:
    m = hashlib.md5()
    m.update(bytes(input + str(index), 'utf-8'))
    s = m.hexdigest()
    if s.startswith("00000"):
        password += s[5]
    index += 1
print("Part 1 Password: " + password)

# Now do the same thing, but the sixth character is the position (array indexing)
# and the seventh is the character to add. Ignore invalid positions. Make it look like
# WarGames. (i.e. Fills it in as it goes.)
# Note: console IO makes the process super slow.

import random
import time
import calendar
random.seed(calendar.timegm(time.gmtime()))

password = list("________")
index = 0
while "_" in password:
    m = hashlib.md5()
    m.update(bytes(input + str(index), 'utf-8'))
    s = m.hexdigest()
    if s.startswith("00000"):
        if s[5].isdigit():
            pos = int(s[5])
            if pos >= 0 and pos <= 7 and password[pos] is "_":
                password[pos] = s[6]
    index += 1
    for c in password:
        if c is "_":
            print(chr(random.randrange(48, 123)), end='')
        else:
            print(c, end='')
    print("", end='\r')
print("Part 2 Password: "+ "".join(password), end='\n')