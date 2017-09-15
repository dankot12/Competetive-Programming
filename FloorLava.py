import sys
sys.setrecursionlimit(45000)
L,B,S = map(int,raw_input().split())
SafeMines = []
for i in range(S):
    SafeMines.append(map(int,raw_input().split()))
    SafeMines[i][0] -= 1
    SafeMines[i][1] -= 1

Mines = []
minescount = 0
for i in range(L):
    row = []
    for j in range(B):
        if [i,j] in SafeMines:
            row.append(1)
            minescount += 1
        else:
            row.append(0)
    Mines.append(row)

def recmines(i,j):
    sum = 0
    if (i<0) or (j<0) or (i>=L) or (j>=B):
        return 0
    elif Mines[i][j] == 0 or [i,j] in MinesList:
        return 0
    else:
        if Mines[i][j] == 1 and [i,j] not in MinesList:
            if (i+1)>=L or Mines[i+1][j]==0:
                sum += 1
            if (j+1)>=B or Mines[i][j+1]==0:
                sum += 1
            if (j-1)<0 or Mines[i][j-1]==0:
                sum += 1
            if (i-1)<0 or Mines[i-1][j]==0:
                sum += 1
            MinesList.append([i,j])
            sum += recmines(i-1,j)+recmines(i+1,j)+recmines(i,j-1)+recmines(i,j+1)
        return sum

count = 0
MinesList = []
for i,j in SafeMines:
    if Mines[i][j] == 1 and [i,j] not in MinesList:
        count = max(count,recmines(i,j))
print MinesList
print count
