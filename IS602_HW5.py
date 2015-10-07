
# coding: utf-8

# ## IS602_HW5
# ### Basic Data Mining - Least Squares Linear Regression
# ### Daina Bouquin

# 1. Download the dataset called "brainandbody.csv" or aquire the data from [here](http://vincentarelbundock.github.io/Rdatasets/datasets.html). This file is a small set of average brain weights and average body weights for a number of animals. We want to see if a relationship exists between the two.
# 2. Perform a linear regression using the least squares method on the relationship of brain weight [br] to body weight [bo]. Do this using just the built in Python functions (this is really easy using scipy, but we're not there yet).  We are looking for a model in the form bo = X * br + Y.  Find values for X and Y and print out the entire model to the console.

# In[86]:

import Tkinter
import tkFileDialog
import csv


# In[87]:

# Bring in the dataset using Tkinter dialog box
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent=root)
filename_open = open(filename)
dataset = list(csv.reader(filename_open))


# In[88]:

dataset[0] 


# In[89]:

# remove the headers for simplicity
del dataset[0]


# In[90]:

dataset[0] 


# Here the body will be the independent variable X and Brain be the dependent variable Y:

# In[91]:

# Find the sum of X
numlist = [float(i[1]) for i in dataset]
x_sum = sum(numlist)
print(x_sum)


# In[92]:

# Find the mean of X
x_mean = x_sum / len(dataset)
print(x_mean)


# In[93]:

# Find the sum of Y
numlist = [float(i[2]) for i in dataset]
y_sum = sum(numlist)
print(y_sum)


# In[94]:

# Find the mean of Y
y_mean = y_sum / len(dataset)
print(y_mean)


# In[95]:

# Find the sum of XY
numlist = [float(i[1])*float(i[2]) for i in dataset]
xy_sum = sum(numlist)
print(xy_sum)


# In[113]:

# Find the slope and round to nearest hundreth
x_b = [float(i[1])-x_mean for i in dataset]
x_b_sum = sum(x_b)
y_b = [float(i[2])-y_mean for i in dataset]
y_b_sum = sum(y_b)

# Slope numerator and denominator
slope_n = [((float(i[1])-x_mean) * (float(i[2])-y_mean)) for i in dataset]
slope_n = sum(slope_n)
slope_d = [((float(i[1])-x_mean)**2) for i in dataset]
slope_d = sum(slope_d)

slope = (slope_n / slope_d)

print "Slope: ", slope_n, "/", slope_d, "=", round(slope, 2)


# In[120]:

# Calculate the intercept and round to nearest hundreth
b_int = round(y_mean - slope * x_mean, 2)
print b_int


# In[121]:

# Print the model to the console:
print "bo = ", round(slope,2), "br +", b_int

