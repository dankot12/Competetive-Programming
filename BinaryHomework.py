import sys

N,Q = map(int,raw_input().split())
S = []
Binary = []
for i in range(N):
    Binary.append('0')
for i in range(Q):
    S.append(map(int,raw_input().split()))

def changer(i,j):
    for k in range(i,(j+1)):
        if Binary[k-1] == 0:
            Binary[k-1] = 1
        else:
            Binary[k-1] = 0

def concat(num):
    k = map(str,num)
    k = ''.join(k)
    return k

Sequences = []

for i in range(Q):
    changer(S[i][0],S[i][1])
    Sequences.append(Binary[:])

print concat(max(Sequences))
