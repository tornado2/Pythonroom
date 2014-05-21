# author: tornado2
people = range (1,101)
switch = False
Round = (1,101)
for r in Round:
	for p in people:
		if p % r == 0:
			if switch == False:
				switch = True
			else:
				switch = False
print switch