import sys

N_cases = raw_input()
list = []
pl1sc = 0
pl2sc = 0
for i in range(int(N_cases)):
	pl1r,pl2r = raw_input().split()
	pl1sc = pl1sc + int(pl1r)
	pl2sc = pl2sc + int(pl2r)
	list.append(pl1sc -pl2sc)

pl1lead = max(list)
pl2lead = min(list) * -1

if pl1lead>pl2lead:
	print "1 ", pl1lead
else:
	print "2 ", pl2lead
