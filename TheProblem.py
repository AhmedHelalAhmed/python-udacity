# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!


#2012 was a leap year
#leap year
#السنة الكبيسة هي سنة عدد أيامها 366 يوم #
# مع العلم أن السنة عدد أيامها 365 يوم
#  ولكن لأن الأرض تستغرق في دورتها حول الشمس 365 يوم وربع اليوم
# فقد تقرر جمع هذه الأرباع واضافتها في السنة الرابعة
# لكي يتناسب التقويم مع الدورة الفلكية.

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
    elif year%400!=400:
        return False
    else:
        return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##

    return days