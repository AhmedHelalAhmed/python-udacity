# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

#print countries[1][1]

for country in countries:
    if country[0] == "India":
        print country[1]
        break


# Note that the capital of India is actually New Delhi
# (which is contained in the region of Delhi).
# In my defense, the capital of the United States is actually the "District of Columbia",
# so at least I am equally wrong for my native country.
