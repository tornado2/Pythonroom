# author: tornado2
time = 0
distance = 0
speed = 100
while distance < 100:
	distance = distance + (speed/12)
	speed = speed - 1
	time = time + 5
print time