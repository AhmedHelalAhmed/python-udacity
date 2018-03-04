# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    # print somestring
    # print sub

    location = somestring.find(sub)
    # print location
    if location == -1 :
        return somestring
    length = len(sub)
    # print length
    part_before = somestring[:location]
    # print part_before
    part_after = somestring[location + length:]
    # print part_after
    return part_before + part_after

#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"
