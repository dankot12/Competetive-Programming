import sys

N = int(raw_input())
Str = ""
for i in range(N):
    Str += raw_input()

Punctuations = ['\'','.',',',';',':']

Str = list(Str)
Words = [x.lower() for x in Str if x not in Punctuations]

Words = ''.join(Words)
Words = Words.split()

Words = list(set(Words))

Words.sort()

print len(Words)
for i in Words:
    print i
