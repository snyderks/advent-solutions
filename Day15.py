discs = []

# Create data
discs.append((13, 11))
discs.append((5, 0))
discs.append((17, 11))
discs.append((3, 0))
discs.append((7, 2))
discs.append((19, 17))
discs.append((11, 0))

done = False
t = 0
while done is False:
    done = True
    for i, disc in enumerate(discs):
        if (t + i + 1 + disc[1]) % disc[0] is not 0:
            done = False
            break
    if done:
        print(str(t))
        break
    t += 1
