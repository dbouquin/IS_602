# something that throws an error
# but we want the program to continue through execution regardless

# Use try / except

'''
file_object = open("testfile.txt", "r") #this throws error bc file does not exist
'''

try:
    file_object = open("testfile.txt", "r")
    x = 5/1
    print "File exists"
except ZeroDivisionError:
    print "Divide by zero found"
except IOError: #this is the type of error that the terminal returns with line 7 command
    print "File not found"

print "Done"

# You can also create a general except statement to handle everything:

try:
    x = 19/0
    file_object = open("testfile.txt", "r")
    x = 5/1
except:
    print "there's a problem"

print "Done"
