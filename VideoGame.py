import sys

width,height = raw_input().split()
boxheight = raw_input().split()
commands = raw_input().split()

i = 0
crane_pos = 0
pick = 0 #flag

#convert inputs from string to int
width = int(width)
height = int(height)
boxheight = [int(x) for x in boxheight]
commands = [int(x) for x in commands]

while i<len(commands):

    if commands[i] == 0:
        break

    if commands[i] == 1:
        if crane_pos!=0:
            crane_pos = crane_pos - 1

    if commands[i] == 2:
        if crane_pos!=(width-1):
            crane_pos = crane_pos + 1

    if commands[i] == 3:
        if pick == 0:
            if boxheight[crane_pos] > 0:
                pick = 1
                boxheight[crane_pos] = boxheight[crane_pos] - 1

    if commands[i] == 4:
        if pick == 1:
            if boxheight[crane_pos] < height:
                pick = 0
                boxheight[crane_pos] = boxheight[crane_pos] + 1

    i = i + 1

print " ".join(str(x) for x in boxheight)
