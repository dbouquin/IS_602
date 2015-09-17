# modules:
import re
import pandas as pd
from pandas import DataFrame
import Tkinter # GUI
import tkFileDialog # dialog box
import csv #for writing csv

'''
This program allows you to feed in a file using a dialog box
The module Pandas is used for I/O, error handling, and sorting
http://pandas.pydata.org/pandas-docs/stable/index.html
'''
# GUI to select file for input
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent=root)

df = pd.read_csv(filename) # store csv as dataframe df

print "1. Reading file from %s" %filename
print "Check Structure:"
print df.head() #check the structure of df

# create objects containing valid values for columns
valid_buying_price = ['vhigh','high','med', 'low']
valid_maintenance_price = ['vhigh','high','med', 'low']
valid_persons = ['2','4','more']
valid_lug_boot = ['small','med','big']
valid_safety = ['low','med','high']
valid_acceptability = ['unacc','acc','good', 'vgood']

# check to see if any columns have invalid entries:

print "Checking for problems:"

# validate values in buying_price
if df['buying_price'].isin(valid_buying_price).all():
    print "No errors in buying_price"
else:
    print "Error: invalid buying_price detected"

# validate values in maintenance_price
if df['maintenance_price'].isin(valid_maintenance_price).all():
    print "No errors in maintenance_price"
else:
    print "Error: invalid maintenance_price detected"

# validate values in persons_capacity
if df['persons_capacity'].isin(valid_persons).all():
    print "No errors in persons_capacity"
else:
    print "Error: invalid persons_capacity detected"

# validate values in lug_boot
if df['lug_boot'].isin(valid_lug_boot).all():
    print "No errors in lug_boot"
else:
    print "Error: invalid lug_boot detected"

# validate values in safety_rating
if df['safety_rating'].isin(valid_safety).all():
    print "No errors in safety_rating"
else:
    print "Error: invalid safety_rating detected"

# validate values in acceptability
if df['acceptability'].isin(valid_acceptability).all():
    print "No errors in acceptability"
else:
    print "Error: invalid acceptability detected"

#2a. Print to the console the top 10 rows of the data sorted by safety in descending order

df_safety_sort = df.sort(columns= "safety_rating", ascending = False)

print "2a. First 10 sorted by safety in descending order:"
print df_safety_sort.head(n=10)

#2b. Print to the console the bottom 15 rows of the data sorted by maintenance in ascending order

df_maint_sort = df.sort(columns= "maintenance_price", ascending = True)

print "2b. Last 15 sorted by maintenance in descending order:"
print df_maint_sort.tail(n=15)

#2c. Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order.
#    Find these matches using regular expressions.

mask = df[['buying_price', 'maintenance_price', 'safety_rating']].apply(lambda x: x.str.contains('vhigh|high', regex=True)).any(axis=1)

print "2c. This is a filtered dataframe sorted by number of doors:"
# sort by doors
print df[mask].sort('doors', ascending=True)

#2d. Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.
# The file path can be a hard-coded location (name it output.txt) or use a dialog box.

part2d = df.query('buying_price == "high" and maintenance_price == "med" and doors == "4" and persons_capacity == "4" or persons_capacity == "more"')

print "This is part 2d that will be written to a csv called 'output.csv':"
print part2d

part2d.to_csv('output.csv')
