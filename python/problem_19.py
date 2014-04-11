def date_generator(start_year):
	year = start_year
	day_num = 1
	day = day_generator("Monday")
	month_gen = month_generator("January")
	month = month_gen.next()
	while True:
		yield (day.next(),day_num,month,year)
		if day_num == 31:
			day_num = 1
			month = month_gen.next()
			if month == "January":
				year += 1
		elif day_num == 30 and month in ["September","April","June","November"]:
			day_num = 1
			month = month_gen.next()
		elif day_num == 28 and month == "February" and not is_leap_year(year):
			day_num = 1
			month = month_gen.next()
		elif day_num == 29 and month == "February" and is_leap_year(year):
			day_num = 1
			month = month_gen.next()
		else:
			day_num += 1

def is_leap_year(year):
	if year % 100 != 0 and year % 4 == 0:
		return True
	elif year % 100 == 0 and year % 400 == 0:
		return True
	return False


def day_generator(start_day):
	days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",
	"Sunday"]
	i = days.index(start_day)
	while True:
		yield days[i%7]
		i += 1

def month_generator(start_month):
	months = ["January","February","March","April","May","June","July","August",
	"September","October","November","December"]
	i = months.index(start_month)
	while True:
		yield months[i%12]
		i += 1

d = date_generator(1900)
date = d.next()
counter = 0
while date[3] != 2001:
	if date[0] == "Sunday" and date[1] == 1:
		print date
		counter += 1
	date = d.next()
print counter