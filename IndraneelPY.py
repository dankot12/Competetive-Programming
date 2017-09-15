import sys

blocks = []
N_blocks = int(raw_input())
for i in range(N_blocks):
    blocks.append(min(map(int,raw_input().split())))

blocks.sort()
k = 1
count = 0
for i in range(N_blocks):
    if k <= blocks[i]:
        blocks[i] = k
        k += 1
    else:
        count += 1

print N_blocks - count
