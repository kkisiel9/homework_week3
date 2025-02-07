#!/usr/bin/python
from dataclasses import replace

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# my main variableabove
string_length = len(Belgium)
# counting the lenght of my main variable
# print(string_length)
print(Belgium)
print("-"*81)
# multiplying the string object -

new_Belgium = Belgium.replace(",",":")
# creating a new variable where by using the replace method I am replacing all of the commas with colons

print(new_Belgium)
print("-"*81)
#here I am adding another line of hyphens
pop_Belgium = Belgium[8:16]
pop_Brussels = Belgium[26:32]
# creating two new varibales and slicing my main string to obtain the desired populations
print(int(pop_Brussels) + int(pop_Belgium))
# formatting my strings to get the desired sum