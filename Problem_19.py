
def daysOnMonth(year, month):
    NAMESOFMONTHS = {0: 'JAN', 1: 'FEV', 2: 'MAR', 3: 'APR', 4: 'MAY', 5: 'JUN', 6: 'JUL', 7: 'AUG', 8: 'SEP', 9: 'OCT', 10: 'NOV', 11: 'DEC'}
    DAYSONREGULARMONTHS = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

    if month==1 and year%4==0:
        if year%100==0 and year%400==0:
            return 29
        elif year%100==0:
            return 28
        else:
            return 29
    else:
        return DAYSONREGULARMONTHS[month]

def daysOnYear(year):
    if year%4!=0:
        return 365
    elif year%100==0 and year%400!=0:
        return 365
    else:
        return 366

def dayOfTheWeek(year, month, day):
    NAMESOFMONTHS = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}

    return (daysSinceBeginning(year, month, day)+1)%7

def daysSinceBeginning(year, month, day):
    days = 0
    for y in range(1900, year):
        days += daysOnYear(y)
    for m in range(0, month):
        days += daysOnMonth(year, m)
    return days+day-1


def main():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(0, 12):
            # for day in range(1, 28):
            if dayOfTheWeek(year, month, 1) == 0:
                sundays += 1
                print(f"{year}-{month+1}-1")
    
    print(sundays)

if __name__ == '__main__':
    main()