def main():
	year = 1900
	month = 1
	months_30 = [4,6,9,11]
	day = 1
	i = 1
	sunday_counter = 0
	while True:
		if month in months_30:
			limit = 30
		elif month == 2:
			limit = 28
			if year%4==0 and year % 100 !=0:
				limit = 29
			if year%400 == 0:
				limit = 29
		else:
			limit = 31
		if i > limit:
			i = 1
			month+=1
		if month>12:
			month = 1
			year+=1
		if day==7:
			if i == 1:
				if year >=1901:
					sunday_counter +=1
			day = 0
		if year > 2000:
			break
		i+=1
		day+=1
	print(sunday_counter)

if __name__ == '__main__':
	main()