import sys

N = int(raw_input())
Average = []
for i in range(N):
    Average.append(int(raw_input()))
Average.sort()

def finder(key):
    mi = 0
    ma = N - 1
    while mi <= ma:
        mid = (mi+ma)/2
        if Average[mid] == key:
            return True
        elif Average[mid] > key:
            ma = mid - 1
        else:
            mi = mid + 1
    return False

i = 0
j = 1
count = 0


print count
