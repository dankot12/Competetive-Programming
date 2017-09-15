import sys

N,M = map(int,raw_input().split())
MulSet = map(int,raw_input().split())
Num = []
for i in range(M):
    Num.append(int(raw_input()))

Res = []
i = 0
maNum = max(MulSet)
while i < maNum:
    num = max(MulSet)
    if (num/2) > 0:
        MulSet[MulSet.index(num)] = num/2
    if (i+1) in Num:
        print num
    i += 1
