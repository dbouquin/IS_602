
# coding: utf-8

# In[8]:

import Tkinter
import tkFileDialog
import mahotas as mh
import pylab


# In[9]:

print "First select the circles.png file using the dialog box"


# In[10]:

# Use the dialog box to bring in the circles.png file:
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent=root)


# In[13]:

def circles():
    # Image 1 is the circles.png file
    my_image = mh.imread(filename)
    # Threshold using the Riddler-Calvard method 
    # More on Riddler-Calvard: http://mahotas.readthedocs.org/en/latest/thresholding.html
    thres = mh.rc(my_image)
    #use the value to form a binary image
    b_image = (my_image > thres)
    #use gaussian filter
    g_image = mh.gaussian_filter(b_image, 33)
    #separate objects stuck together
    rmax = mh.regmax(g_image)
    #count the number of objects in the picture
    labeled, nr_objects = mh.label(rmax)
    #find center point for each object
    centers = mh.center_of_mass(my_image, labeled)[1:]
    print "The circles.png file contains ", nr_objects, " objects."
    o = 1
    for center in centers:
        print "Object %s center: %s" %(o, center)
        o = o + 1


# In[14]:

circles()


# In[15]:

print "Next run the same tests on the objects.png file by selecting it using the dialog box"


# In[16]:

# Use the dialog box to bring in the objects.png file:
root = Tkinter.Tk()
root.withdraw()
filename2 = tkFileDialog.askopenfilename(parent=root)


# In[17]:

def objects():
    # The second image is the objects.png file
    #import image from file
    my_image = mh.imread(filename2)
    #use the mean to form a binary image
    b_image = (my_image > my_image.mean())
    #use gaussian filter
    g_image = mh.gaussian_filter(b_image, 1.5)
    #count the number of objects in the picture
    labeled, nr_objects = mh.label(g_image)
    #find center point for each object
    centers = mh.center_of_mass(my_image, labeled)[1:]
    print "The objects.png contains ", nr_objects, " objects."
    o = 1
    for center in centers:
        print "Object %s center: [ %s, %s ]"               %(o, round(center[1], 0), round(center[0], 0))
        o = o + 1


# In[18]:

objects()


# In[19]:

print "Last we test the peppers.png file by selecting it using the dialog box"


# In[20]:

# Use the dialog box to bring in the peppers.png file:
root = Tkinter.Tk()
root.withdraw()
filename3 = tkFileDialog.askopenfilename(parent=root)


# In[21]:

def peppers():
    # This last image is the peppers.png file
    my_image = mh.imread(filename3)
    T = mh.otsu(my_image)
    b_image = (my_image > T)
    g_image = mh.gaussian_filter(b_image, 15)
    rmax = mh.regmax(g_image)
    labeled, nr_objects = mh.label(rmax)
    centers = mh.center_of_mass(my_image, labeled)[1:]
    print "The peppers.png file contains ", nr_objects, " objects."
    o = 1
    for center in centers:
        print "Object %s center: [ %s, %s ]"               %(o, round(center[1], 0), round(center[0], 0))
        o = o + 1


# In[22]:

peppers()

