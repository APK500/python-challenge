# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:26:06 2018

@author: Adam Knapp
"""
***************************************************
#****PULLING IN TEXT FORMAT ___ FYI only, not for HW specifically

#Store the file path associated with the file (note the backslash may be OS specific) 
file = 'desktop/aapl.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)

*****************************************************

    
METHOD 1 PULLING IN CSV ROWS    
# METHOD 1 OF PULLING IN CSV ROWS 
    
import os
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')


# # Method 1: Plain Reading of CSVs
with open(csvpath, 'r') as file_handler:
   lines = file_handler.read()
   print(lines)
   print(type(lines))
    
 

 ****************************************************************   
    
BEST METHOD FOR HW-- PULLING IN CSV AND PRINTING DATA AND ROWS!!    
 
import os
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        print(row)
#CODE PRINTS TOTAL NUMBER OF ROWS        
    print("Total no. of rows: %d"%(csvreader.line_num))