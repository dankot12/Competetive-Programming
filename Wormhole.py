import sys

N_exams,N_St,N_End = map(int,raw_input().split())
Exams = []
for i in range(N_exams):
    Exams.append(map(int,raw_input().split()))

Start = map(int,raw_input().split())
Start.sort()

End = map(int,raw_input().split())
End.sort()

def minstart(start):
    mini = 0
    maxi = N_St - 1
    while mini <= maxi:
        mid = (mini + maxi)/2
        if Start[mid] == start:
            return Start[maxi]
        if Start[mid] > start:
            maxi = mid - 1
        else:
            mini = mid + 1
    return Start[maxi]

def minend(end):
    mini = 0
    maxi = N_End - 1
    while mini <= maxi:
        mid = (mini + maxi)/2
        if End[mid] == end:
            return End[mini]
        if End[mid] > end:
            maxi = mid - 1
        else:
            mini = mid + 1
    return End[mini]

i = 0
count = []
while i < N_exams:
    mi = Exams[i][0]
    if mi < Start[0]:
        i += 1
        continue
    ma = Exams[i][1]
    if ma > End[N_End - 1]:
        i += 1
        continue
    st = minstart(mi)
    ed = minend(ma)
    count.append(ed - st + 1)
    i += 1

print min(count)
