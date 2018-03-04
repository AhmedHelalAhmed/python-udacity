# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(number1,number2,number3):
    biggest_number=biggest(number1,number2,number3)
    if biggest_number == number1 :
        second_greater_one=bigger(number2,number3)
        if second_greater_one == number2 :
            return number2
        else :
            return number3
    elif biggest_number == number2:
        second_greater_one = bigger(number1,number3)
        if second_greater_one == number1 :
            return number1
        else :
            return number3
    else :
        second_greater_one = bigger(number1,number2)
        if second_greater_one == number1 :
            return number1
        else :
            return number2








print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







