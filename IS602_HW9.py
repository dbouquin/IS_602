
# coding: utf-8

# <h3>HW9: Working with Pandas Dataframes</h3> 
# 
# Use the pandas module to answer the following questions about the EPA-HTTP data set.  Print the result of each part to the console.  Use pandas as much as you can; this includes the data structure and the analysis.

# In[36]:

import re
import pandas as pd
import numpy as np
from StringIO import StringIO
import Tkinter
import tkFileDialog


# In[45]:

def data_clean(data_file):
    """
    restructure the epa-http.txt file "HW9_data.txt" locally
    input: text file from local system selected using dialog box
    returns: pandas dataframe with and correct timestamp and quoting
    """

    pattern = r"(\" )(?=HTTP)"  # filter triple quoted lines

    with open(data_file) as d:
        raw = d.read()

    f_txt = re.sub(pattern, " ", raw) # removes the extra quote

    x = StringIO(f_txt) # load the data into StringIO

    df = pd.read_csv(x, sep="\s+", header=None, na_values="-")  # separate by space.
    df.columns = ['IP_address', 'time_stamp', 'request', 'status', 'bytes']

    df['time_stamp'] += "1995-08" # add year and month
    df['time_stamp'] = pd.to_datetime(df['time_stamp'], format="[%d:%H:%M:%S]%Y-%m")

    return df


# In[38]:

# Select file using dialog box
root = Tkinter.Tk()
root.withdraw()
file_p = tkFileDialog.askopenfilename(parent=root)


# In[39]:

# clean up the file using data_clean()
new_data = data_clean(file_p)

# check to make sure it's structured properly
print new_data[:5]


# In[40]:

# 1. Which hostname or IP address made the most requests?
print "IP_address or hostname with most requests:"
print new_data['IP_address'].value_counts()[:1]


# In[41]:

# 2. Which hostname or IP address received the most total bytes from the server? How many bytes did it receive?
ip_1 = new_data.groupby(new_data.IP_address)
byte_totals = ip_1['bytes'].aggregate(np.sum)
byte_totals.sort(inplace=True, ascending=False)
print "IP_address and hostname with most total bytes:"
print byte_totals[:1]


# In[42]:

#3. During what hour was the server the busiest in terms of requests?
time_1 = new_data.groupby(new_data['time_stamp'].dt.hour)
group_size = time_1.size()
group_size.sort(inplace=True, ascending=False)
print "Busiest server hour | number of requests:"
print "                 " + str(group_size[:1]) 


# In[43]:

#4 Which .gif image was downloaded the most during the day?
s = new_data[(new_data.status == 200) & (new_data.request.str.contains('\\.gif'))]
print "                Most downloaded gif image | download count"
print sub.request.value_counts()[:1]


# In[44]:

#5 What HTTP reply codes were sent other than 200?
http_s = new_data[new_data.status != 200]
print "Codes | counts:"
print http_s.status.value_counts()

