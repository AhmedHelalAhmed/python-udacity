# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!


#2012 was a leap year
#leap year

months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def daysInMonth(month,year):
    #if month in (1,2,3,5,7,8,10,12)
    if month == 1 or month == 3 or month == 5 or month ==7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2 :
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(month,year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    #tests
    assert daysBetweenDates(2013,1,1,2013,1,1)==0
    assert daysBetweenDates(2013,1,1,2013,1,2)==1
    assert nextDay(2013,1,1)==(2013,1,2)
    assert nextDay(2013,4,30)==(2013,5,1)
    assert nextDay(2012,12,31)==(2013,1,1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    assert daysBetweenDates(2013,1,1,2014,1,1) == 365
    assert daysBetweenDates(2013, 1, 24, 2013, 6, 29) == 156
    print "Tests done"

test()

# draft
# (day1,month1,year1,day2,month2,year2)
# (24,1,2013,29,6,2013)
# 29/6/2013
# 24/1/2013
# ===========
# january => 24-31=7
# where 31 is the days in january
# february => 28
# march => 31
# april => 30
# may => 31
# june => 29
# ===========
# 156 days
# ===========
# days between this dates
# 5/5/0
# ===========
# for years
# 2013 - 2024
# leap year => 366
# normal year => 365
# 2013 => 365
# 2024 => 366
# ===========
# (day1,month1,year1,day2,month2,year2)
# algorithm
# days = #of days in month1 - day1
# days = 31 - 24 = 7
# month1 + = 1
# while month1 < month2 :
#       days + =# of days in month1
#       month1 + = 1
# days + = day2
# while year1 < year2 :
# 	add number od days at that year
# ===========
