import  sys

cards = map(int,raw_input().split())

count = 0
cards.sort()

temp = int()
oldkey = int()

for i in range(4):
    for j in range(i+1,5):
        if cards[i] == cards[j]:
            count += 1

for i in range(1 << 5):
    c = [cards[j] for j in range(5) if (i & (1 << j))]
    if sum(c) == 15:
        count += 1


print count
