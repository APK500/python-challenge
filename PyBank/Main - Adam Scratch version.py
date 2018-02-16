# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:26:06 2018

@author: Adam Knapp
"""

#CODE BELOW is for the count function  (using the text file format)

#Store the file path associated with the file (note the backslash may be OS specific) 
file = 'desktop/aapl.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)


# get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    
    
#  ************************************************************************  
    
import os
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')


# # Method 1: Plain Reading of CSVs
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))