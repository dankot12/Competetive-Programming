import sys
import itertools

K = []
for line in sys.stdin:
    K = K + line.split()
T = int(K.pop())
S = int(K.pop())
Range = [list(x) for x in K[2:]]

def lookout(lst):
    count = 0
    for i in lst:
        j = 0
        sum = 0
        x = list(lst)
        while j<len(x):
             if x[j] == 0:
                 if sum>0:
                     if sum%S!=0:
                        break
                     else:
                         sum = 0
             else:
                 sum += 1
             j += 1
        if sum%S!=0:
            continue
        count += 1
    return count

for t in range(T):
    lst = []
    for i in range(Range[t][0],Range[t][1]+1):
        lst = itertools.product([0, 1], repeat=i)
        count += lookout(lst)
    print count
