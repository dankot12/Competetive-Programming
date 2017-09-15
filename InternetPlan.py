import sys

Q = int(raw_input())
M = int(raw_input())
count = 0
for i in range(M):
    count += Q - int(raw_input())

print count + Q
