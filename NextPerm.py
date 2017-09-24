import sys

N,K = map(int,raw_input().split())

orig = [x+1 for x in range(N)]

def Perm(per,n):
    k = range(n)
    k.sort(reverse = True)
    for i in k:
        if per[i] > per[i-1]:
            a = i - 1
            break
    j = n-1
    while j > a:
        if per[j] >= per[a]:
            per[j],per[a] = per[a],per[j]
            per[a+1:n] = per[n-1:a:-1]
            break
        j -= 1
    return per

for j in range(K):
    per = map(int,raw_input().split())
    per = Perm(per,N);
    for x in per:
        print x,
    print

sys.exit(0)
