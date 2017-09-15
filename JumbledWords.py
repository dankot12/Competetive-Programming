import sys

S = map(str,raw_input().split())
sure = map(str,raw_input.split())

size = len(S)
sizelstlen = list(size)
acsize = list(size - len(sizelstlen))
for i in acsize:
    S.remove(i)

for i in sure:
    S.remove(i)

S.sort()

def second_smallest(numbers):
    m1, m2 = str('99'), str('99')
        for x in numbers:
            if x <= m1:
                m1, m2 = x, m1
            elif x < m2:
                m2 = x
    return m2

if S[0] == 0:
    ss = second_smallest(S)
    S[S.index(ss)],S[0] = S[0],S[S.index(ss)]

start = len(S) - S[::-1].index(S[0])

Seq = []
m = str(sure)
for i in range(start,len(S))
    Seq.append(''.join(S[:start])+m+''.join(S[start:]))

print min(Seq)
