# input directly with console using "raw_input"

'''
input1 = raw_input("Enter some input: ")
input2 = raw_input("Enter more input: ")

print input1 + input2
'''

# working with files using "open"
'''
file_object = open("foo_ex.txt", "r" ) # must enter "access mode" (i.e. read/r, write/w, apend/a)
print "Name of file ", file_object.name
print "Mode ", file_object.mode # refers to the access mode of the object

# using close - check to see if the file is closed using .closed
print "Is closed: ", file_object.closed
file_object.close()
print "Is closed: ", file_object.closed
'''

#  using append to write a new line of text
'''
file_object = open("foo_ex.txt", "a" )
file_object.write("\nThis is from my program.\n") #\n means write a new line
file_object.close()
'''
# using write to overwrite file with new information
'''
file_object = open("foo_ex.txt", "w" )
file_object.write("This is also from my program")
'''
# using read to read a specific amount of the file
'''
file_object = open("foo_ex.txt", "r" )
content = file_object.read(17) # we can set other parameters here (e.g. only read 17 bytes)
print content
file_object.close()
'''

# using os module
import os
dir(os)
# help(os) to view manual- use q to exit python help in terminal

#use the os module to rename a file
'''
os.rename("foo_ex.txt", "bar_ex.txt")
'''

# use os to make a new directory
#os.mkdir("newdirectory")
# remove that directory
os.rmdir("newdirectory")
