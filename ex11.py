#!/usr/bin/python

# Belgium is the variable name
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# print and len are both functions
# '_' is a string that gets printed the number of times the length of the Belgium string
print('_' * len(Belgium))

# .replace is a method and Belgium is the variable
# the old is ',' which is split by a comma to show the new which is ":'
print(Belgium.replace(',', ':'))


# .split is another method to convert the string into a list.
# the (',') tells the string to be divided everytime there is a comma in the original Belgium string
# I have created a new variable of the Belgium string as a list called fields
list = Belgium.split(',')
print(list)

# a new variable
# int is a function to convert ths string into the integer
# the square brackets with number finds the fields I want added up, the first field is always 0
total_population = int(list[1]) + int(list[3])
print(total_population)



