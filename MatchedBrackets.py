import sys

N_Brack = int(raw_input())

Brackets = []
Brackets = map(int,raw_input().split())

max_count = 0
best_count = 0
brack_stacks = 0
count_start = 0
best_start = 0
nest_depth = 0
best_depth = 0
best_nest_start = 0

for i in range(N_Brack):
    if brack_stacks == 0:
        count_start = i + 1
        max_count = 0

    if Brackets[i] == 1:
        nest_depth += 1
        max_count += 1
        brack_stacks += 1
        if nest_depth > best_depth:
            best_depth = nest_depth
            best_nest_start = i + 1

    if Brackets[i] == 2:
        nest_depth -= 1
        max_count += 1
        brack_stacks -= 1
        if max_count > best_count:
            best_count = max_count
            best_start = count_start

print best_depth, best_nest_start, best_count, best_start
