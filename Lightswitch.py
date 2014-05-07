# author: tornado2
day = 1
month = 1
year = 1900
total = 0
while year < 2015:
	total = total + 1
	if month == 2:
		if day == 28:
			day = 1
			month = month + 1
		else day = day + 1
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		if day == 31:
			day = 1
			month = month + 1
		else day = day + 1	
			if month == 13:
				month = 1
				year = year + 1
		if month == 4 or month == 6 or month == 9 or month == 11:
			if day == 30:
				day = 1
				month = month + 1
			else day = day + 1
			
		
print str(total) + " days."	
