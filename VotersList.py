import sys

l1,l2,l3 = raw_input().split()

VotersList = []
for i in range(int(l1)+int(l2)+int(l3)):
    VotersList.append(raw_input())

oldkey = -1
temp = -1
UpdatedVotersList = []
VotersList.sort()

NewList = [int(x) for x in VotersList]

for x in NewList:
    newkey = x
    if temp == newkey:
        continue
    if oldkey == newkey:
        UpdatedVotersList.append(x)
        temp = newkey
    oldkey = newkey

UpdatedVotersList.sort()
print len(UpdatedVotersList)
for x in UpdatedVotersList:
    print x
