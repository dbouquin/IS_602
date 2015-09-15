# open dialog box
'''
import Tkinter
import tkFileDialog

root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent = root)
print filename
'''
# regular expressions

import re

pattern = '(?<=abc)def'
data = 'abcdef'

m = re.search(pattern, data)
print m.group(0) # first match
