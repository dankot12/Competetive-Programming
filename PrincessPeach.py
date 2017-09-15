import sys

N = int(raw_input())
Tiles = []
for i in range(N):
    Tiles.append(int(raw_input()))

i = 0
count = 0
while (i+2) < N:
    if Tiles[i+2] == 0:
        count += 1
        i += 2
    else:
        count += 1
        i += 1

if i != (N-1):
    count += 1
print count
