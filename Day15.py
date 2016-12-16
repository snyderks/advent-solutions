import queue

discs = []

def genDisk(positions, initPos):
    pos = []
    for i in range(0, positions):
        if i is not 0:
            pos.append(False)
        else:
            pos.append(True)
    return [pos, initPos]

# Create data
discs.append(genDisk(5, 4))
discs.append(genDisk(2, 1))

# Do this by 