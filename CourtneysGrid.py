import sys

K = []
for line in sys.stdin:
    K = K + line.split()

M = int(K[0])
N = int(K[1])
Grid = [list(x) for x in K[2:]]
count = 0
i = 0
while True:
    if i < len(Grid):
        Gridnew = Grid[:]
        Gridnew.sort()
        if Gridnew[:] != Grid[:]:
            Gridnew = map(list,zip(*Gridnew))
            Grid = map(list,zip(*Grid))
            Gridnew[i].sort()
            if Gridnew[i]!=Grid[i]:
                del Gridnew[i]
                del Grid[i]
                count += 1
            else:
                i += 1
                Gridnew = map(list,zip(*Gridnew))
                Grid = map(list,zip(*Grid))
                continue
            Gridnew = map(list,zip(*Gridnew))
            Grid = map(list,zip(*Grid))
            print Gridnew
            print Grid
        else:
            break
    else:
        break

print count
