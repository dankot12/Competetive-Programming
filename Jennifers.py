import sys
import itertools

IN = map(int,raw_input().split())
X = IN[0]
Y = IN[1]
A = IN[2]
B = IN[3]

Class = [list(i) for i in itertools.product([0, 1], repeat=(X+Y)) if list(i).count(1) == X]
count = 0
for i in range(len(Class)):
    mc = 0
    fc = 0
    j = 0
    for j in range(X+Y):
        if Class[i][j] == 0:
            mc = 0
            fc += 1
            if fc > B:
                break
        else:
            fc = 0
            mc += 1
            if mc > A:
                break
    if mc<=A and fc<=B:
        count += 1

print count
