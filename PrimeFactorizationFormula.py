#!/bin/python3

# Prime Factorization 
# For more info: https://mathworld.wolfram.com/PrimeFactorization.html

import sys
input_number=(input("Please provide an integer:\n"))

# Ensure that the user has inserted an integer  
try:
    value = abs(int(input_number))
except ValueError:
    print("-----> Error:You haven't provided an integer")
    sys.exit(2)

input_number = value
division =2 # We start with division = 2 and we will increase if needed
list=[]

while division <= value:
    if (value%division) == 0:
        list.append(division)       #If the number is divided, we add it to the list
        value=value//division       #And we continue with the remaining number
    else: 
            division+=1             #If the number is not devided, we increase divider by one

print("The factors of " +str(input_number) +" are:") 
print(list)
