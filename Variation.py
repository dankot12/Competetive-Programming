import sys
import time

N_seq,Var = map(int,raw_input().split())
Seq = map(int,raw_input().split())

Seq.sort()
count = 0
i = 0
j = 1
while (i < N_seq) & (j<N_seq):
    if abs(Seq[i] -Seq[j]) >= Var:
        count += N_seq - j
        i += 1
    else:
        j += 1
print count
