import sys

N = int(raw_input())
Time = []
for i in range(N):
    Time.append(map(int,raw_input().split()))

TimeNew = []

for i in range(N):
    TimeNew.append([Time[i][1]+Time[i][2],Time[i][0],i])

TimeNew.sort(reverse = True)

bef = 0
best = 0
for i in range(N):
    current = bef + sum(TimeNew[i][0:2])
    bef += TimeNew[i][1]
    best = max(best,current)

print best
