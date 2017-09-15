import sys

L,B,S = map(int,raw_input().split())
SafeMines = []
for i in range(S):
    SafeMines.append(map(int,raw_input().split()))
    SafeMines[i][0] -= 1
    SafeMines[i][1] -= 1

Mines = []
MinesList = []
for i in range(L):
    row = []
    for j in range(B):
        if [i,j] in SafeMines:
            row.append(1)
            MinesList.append([i,j])
        else:
            row.append(0)
    Mines.append(row)

for i,j in MinesList:
    sum = 0
    if (i+1)>=L or Mines[i+1][j]==0:
        sum += 1
    if (j+1)>=B or Mines[i][j+1]==0:
        sum += 1
    if (j-1)<0 or Mines[i][j-1]==0:
        sum += 1
    if (i-1)<0 or Mines[i-1][j]==0:
        sum += 1
    Mines[i][j] = sum

def recmines(i,j):
    sum = 0
    if (i<0) or (j<0) or (i>=L) or (j>=B):
        return 0
    elif Mines[i][j] == 0 or [i,j] in MinesListNew:
        return 0
    else:
        sum = Mines[i][j]
        MinesListNew.append([i,j])
        sum += recmines(i-1,j)+recmines(i+1,j)+recmines(i,j-1)+recmines(i,j+1)
        return sum

count = 0
for i,j in MinesList:
