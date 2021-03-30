# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year_months =      [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_months = [31,29,31,30,31,30,31,31,30,31,30,31]
leaps = { n for n in range(1901,2001) if n%4==0 and not (n%100==0 and n %400 >0 ) }

num_sundays = 0
sunday = 6 # Sunday 6 Jan 1901

for year in range(1901,2001):
    for month in leap_year_months if year in leaps else year_months:
        days_remaining = month - sunday 
        sunday = 7 - (days_remaining % 7) 
        if sunday == 1: num_sundays += 1
    
print(num_sundays)