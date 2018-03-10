# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(input_list,input_element):
    index=0
    find_status=-1
    for element_list in input_list:
        if element_list == input_element:
            find_status=index
            break
        index+=1
    return find_status






print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1