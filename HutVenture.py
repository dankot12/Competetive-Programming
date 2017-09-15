import sys

N = int(raw_input())
P = map(int,raw_input().split())
D = map(int,raw_input().split())

hut = []
for i in range(N):
    j = i + 1
    petrol = 0
    while(j != i):
        petrol += P[j-1]
        if D[j-1] > petrol:
            break
        else:
            petrol -= D[j-1]
            j+= 1
            j = j%N
            if j == i:
                    hut.append(i+1)

P = list(reversed(P))
D = list(reversed(D))
k = D[0]
for i in range(N):
    D[i] = D[i+1]
D[N-1] = k
for i in range(N):
    j = i + 1
    petrol = 0
    while(j != i):
        petrol += P[j-1]
        if D[j-1] > petrol:
            break
        else:
            petrol -= D[j-1]
            j+= 1
            j = j%N
            if j == i:
                    hut.append(abs(N-i-i)+1)

hut = list(set(hut))
print len(hut)
hut.sort()
for i in range(len(hut)):
    print hut[i],
