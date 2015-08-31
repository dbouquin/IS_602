# Daina Bouquin
# IS 602 Homework 1

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
'''
I used "Insertion Sort" with Python via Khan Academy:
https://www.youtube.com/watch?v=lEA31vHiry4
'''
num_list = [22,14,110,27]

def sortwithloops(list):
    for index in range(1,len(list)): #start at 2nd element to left to give comparison
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i] #shift number in slot i right to slot i+1
                list[i] = value #shift value left into slot i
                i = i - 1
            else:
                break
    return list

sortwithloops(num_list)
print(num_list)

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop

num_list2 = [77,12,15,29,880]

def sortwithoutloops(input):
    loopsorted_num_list = input.sort()
    return input

print(sortwithoutloops(num_list2))

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions

num_list3 = [44,2,175,87,1800]

def searchwithloops(input, value):
    while value in input:
        return("True")
    else:
        return("False")

print searchwithloops(num_list3, 99)

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop

num_list4 = [999,26,155,80,1654]

def searchwithoutloops(input, value):
    if value in input:
        return "True"
    else:
        return "False"

print(searchwithoutloops(num_list4,29))

# Check all?
if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]

    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
