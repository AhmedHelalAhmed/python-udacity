# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b


def printInches(n):
    #print n + " inches" ----> the problem
    print str(n) + " inches" #----> the fix


# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)