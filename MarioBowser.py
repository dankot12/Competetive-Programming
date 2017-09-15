import sys
import itertools

K = []
for line in sys.stdin:
    K = K + line.split()
N_Per = int(K.pop(0))
Per = []
for i in range(N_Per):
    Per.append(int(K.pop(0)))
T = int(K.pop(0))
Traps = []
for i in range(T):
    Traps.append(int(K.pop(0)))

Permut = itertools.permutations(Per, N_Per)

count = 0
for i in Permut:
    x = list(i)
    j = 0
    Pos = 0
    F = 0
    for j in range(len(x)):
        Pos += x[j]
        if Pos in Traps:
            F = 1
            break
    if F != 1:
        count += 1

print count%1000000007
