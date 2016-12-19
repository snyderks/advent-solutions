from collections import Counter

startRow = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
rowLength = len(startRow)

trap = "^"
safe = "."

def check(left, center, right):
    if center is trap:
        if left is trap and right is safe:
            return trap
        elif right is trap and left is safe:
            return trap
        else:
            return safe
    elif left is trap and center is safe and right is safe:
        return trap
    elif right is trap and center is safe and left is safe:
        return trap
    else:
        return safe

def checkAny(row, column, rows):
    if column is rowLength - 1:
        return check(rows[row-1][column-1], rows[row-1][column], safe)
    if column is 0:
        return check(safe, rows[row-1][column], rows[row-1][column+1])
    else:
        return check(rows[row-1][column-1], rows[row-1][column], rows[row-1][column+1])

def getRow(row, allRows):
    newRow = ""
    for i in range(0, rowLength):
        newRow += checkAny(row, i, allRows)
    return newRow

def countSafe(rows):
    safes = 0
    for row in rows:
        safes += Counter(row)[safe]
    return safes

rows = [startRow]

for i in range(1, 40):
    rows.append(getRow(i, rows))

for row in rows:
    print(row)

print("Safe tiles: " + str(countSafe(rows)))

# Part 2

rows = [startRow]
safes = 0
for i in range(0, 400000):
    safes += countSafe(rows)
    rows = [getRow(1, rows)]

print("Safe tiles: " + str(safes))
