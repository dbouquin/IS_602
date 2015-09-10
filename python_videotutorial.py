# up to 25 mins on tutorial: https://www.youtube.com/watch?v=N4mEzFDjqtA

import random
import sys
import os

print("Hello World")

# one-line comment
'''
multi-line
comment
'''

name = "Daina Rose"
print(name)

'''
Data Types in Python:
Numbers, Strings, Lists, Tuples, Dictionaries

Operators:
+ - * / %(remainder of a division) **(exponential) //(floor division -- no remainder round down)
'''

print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Order of operation matters
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# Putting a quote inside a string (which is closed with quotes)
quote = "\"Always remember you are unique"
multi_line_quote = ''' just like
everyone else" '''

new_string = quote + multi_line_quote

print(new_string)

print("%s %s %s" %('I like the quote', quote, multi_line_quote))

# End line breaks
print("I don't like ", end = "")
print("new lines")

# Print 5 blank lines-- new lines with \n
print('\n' * 3)

'''
Practice with Lists now

* All Python list indices start at 0 *
'''

grocery_list = ['Juice', 'Potatoes', 'Bananas',
                'Tomatoes']

print('First Item:', grocery_list[0])

# Change list item
grocery_list[0] = 'Green Juice'
print('First Item:', grocery_list[0])

print(grocery_list[1:3])

# Add list to list
other_events = ['Wash car', 'Cash check', 'Laundry']

to_do_list = [other_events, grocery_list]

print(to_do_list)

# print second item in second list
print((to_do_list[1][1]))

# Adding to list
grocery_list.append('Onions')
print(grocery_list)

# Using "insert" to add item to list at certain index
grocery_list.insert(1, "Pickle")
print(grocery_list)

# Remove item
grocery_list.remove("Pickle")
print(grocery_list)

# Sort list (done alphabetically here)
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)

# Length, min, max with lists
print(len(to_do_list))
print(max(to_do_list)) # "highest" alphabetically
print(min(to_do_list))

'''
Tuples
Cannot be changed after created
'''

pi_tuple = (3,1,5,1,5,9)

# You can convert tuple into list if needed and make changes (not normally done)

# Length, max, min with tuple the same
print(len(pi_tuple))
print(max(pi_tuple))
print(min(pi_tuple))

'''
Dictionaries aka "maps":
values with unique key for each stored value -- cannot join these together like lists
'''

super_villians = {'Riddler': 'Issac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon'}

# print the "secret ID"
print(super_villians['Captain Cold'])

# delete entry
del super_villians['Riddler']
print(super_villians)

# length of dictionary
print(len(super_villians))

print(super_villians.get('Captain Cold'))

print(super_villians.keys())

print(super_villians.values())

'''
Conditionals:
if, else, elif, ==, !=, >, >=, <, <=
'''

# make some space
print('\n' * 2)

# white space is used to group blocks of code

age = 30

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

print('\n' * 1)

age2 = 15

if age2 >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age2 >= 16 :
    print('You are old enough to drive a car')
else : print("You are not old enough to drive")

# logical operators: and, or, not
print('\n' * 1)

if ((age >= 1) and (age <= 18)):
    print("You get a party")
elif(age== 21) or (age >= 65):
    print("You get a party")
elif not(age == 30):
    print("You don't get a party")
else:
    print("You get a party - hooray!")

# ^ Once an above condition is met the rest is not run

'''
Looping: repeat action set number of times
For and While loops
'''
print('\n')

#for loop

for x in range(0,10):
    print(x, ' ', end="")

print('\n')

grocery_list = ['Juice','Tomatoes', 'Potatoes',
                'Bananas']

for y in grocery_list:
    print(y)

print('\n')

for x in [2,4,6,8,10]:
    print(x)

print('\n')

num_list = [[1,2,3],[10,20,30], [110,220,330]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# while  - no idea how many times you'll need to loop

print('\n')

random_num = random.randrange(0,100) # 0-99

# while it doesn't equal 15
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

# use iterator and loop to print all even numbers
print('\n')

i = 0

while(i <= 20):
    if(i%2 == 0): # no remainder after dive by 2 tells us we have an even number
        print(i)
    elif(i==9):
        break
    else:
        i += 1 #same as i = i+1
        continue
    i += 1

'''
Functions:
helps us write and re-use more readable code
'''

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,4))
