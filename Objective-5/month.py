months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("What is the year: "))
monthsNum = int(input("What is the number of the month you want: "))


days = 29 if monthsNum == 2 and year % 4 == 0 else None



print(f'month {monthsNum} has {months[monthsNum - 1] if days == None else days} days')