"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless
it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

def date(month, year):
    if month == 1 and year == 1901:
        return 26
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if year % 4 == 0:
            return 29
        else:
            return 28


def cycle():
    firstday = 0
    firstSunday = 0
    for year in range(1901, 2001):  
        for month in range(1, 13): 
            days = date(month, year)
            print("month {} year {}".format(month, year))
            firstday = firstday + days
            if firstday % 7 == 0:
                firstSunday += 1
            else:
                firstday = firstday % 7
    return firstSunday


if __name__ == '__main__':
    numOfSundays = cycle()
    print("Number of Sundays that fell on the first of the month during the twentieth century: {}".format(numOfSundays))
