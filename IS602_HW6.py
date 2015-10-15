import timeit

# Daina Bouquin
# IS 602 Homework 6 - Building on HW1.
# Replace sorting and searching functions with numpy functions
# Time the functions using a large number of tests -- at least 10,000

setup = '''
import copy
import numpy as np
import numpy.random as npr
import random # Generate random numbers with numpy for examples

# 1 from HW1 - sort with loops

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

# 2 from HW1 - sort without loops

def sort_woloops(list):
 list.sort()
 return(list)

# sorting with numpy

def sortwithnumpy(input):
    return np.sort(input)

# 3 from HW1 - search with loops

def searchwithloops(input, value):
    while value in input:
        return("True")
    else:
        return("False")

# 4 from HW1 - search without loops

def search_woloops(input, value):
    if value in input:
        return "True"
    else:
        return "False"

# searching with numpy
def searchwithnumpy(input, value):
    return(len(np.where(input == value)[0]) > 0)

# Create the datasets for testing
# Generate array of 500 elements
np_arr = np.random.permutation(np.arange(500))[:]
list = np_arr.tolist()

# Generate array of 1500 elements - larger to see differences
np_arr = np.random.permutation(np.arange(1500))[:]
list2 = np_arr.tolist()

# Generate random number to search for between 0 and 3000
rand = random.randrange(0,300)
'''

if __name__ == "__main__":

    n = 10000
# small dataset
    print "## Testing small dataset ##"
    t = timeit.Timer("x = copy.copy(list); sortwithloops(x)", setup = setup)
    print "sortwithloops    : ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(list); sort_woloops(x)", setup = setup)
    print "sort_woloops     : ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(np_arr); sortwithnumpy(x)", setup = setup)
    print "sortwithnumpy    : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(list); y = copy.copy(rand); searchwithloops(x,y)", setup = setup)
    print "searchwithloops  : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(list); y = copy.copy(rand); search_woloops(x,y)", setup = setup)
    print "search_woloops   : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(np_arr); y = copy.copy(rand); searchwithnumpy(x,y)", setup = setup)
    print "searchwithnumpy  : ", t.timeit(n), " seconds"

    print "## Testing larger dataset ##"
    t = timeit.Timer("x = copy.copy(list2); sortwithloops(x)", setup = setup)
    print "sortwithloops    : ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(list2); sort_woloops(x)", setup = setup)
    print "sort_woloops     : ", t.timeit(n), " seconds"
    t = timeit.Timer("x = copy.copy(np_arr); sortwithnumpy(x)", setup = setup)
    print "sortwithnumpy    : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(list2); y = copy.copy(rand); searchwithloops(x,y)", setup = setup)
    print "searchwithloops  : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(list2); y = copy.copy(rand); search_woloops(x,y)", setup = setup)
    print "search_woloops   : ", t.timeit(n), " seconds"
    t = timeit.Timer("x=copy.copy(np_arr); y = copy.copy(rand); searchwithnumpy(x,y)", setup = setup)
    print "searchwithnumpy  : ", t.timeit(n), " seconds"
