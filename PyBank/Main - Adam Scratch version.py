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
   Total_Months.append(row[0])
   
  
  str(len(Total_Months))
 

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
    str(len(Total_Months))


#CODE PRINTS TOTAL NUMBER OF ROWS        
    print("Total no. of rows: %d"%(csvreader.line_num))
    
    
    ***********************************************************
    
BEST METHOD FOR HW-- PULLING IN CSV AND PRINTING DATA AND ROWS!!  
SECOND VERSION WITHOUT ALL LINE ITEMS -- TOTALS ONLY
DOESNT TOTAL PROPERLY  
 
import os
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    for row in csvreader:
     print("Total no. of rows: %d"%(csvreader.line_num))
    





****************************************************
Alternate version from geeks site

# importing csv module
import csv
import os
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')
 

import csv
# csv file name
filename = "Desktop/python-challenge/PyBank/budget_data_1.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = csvreader.next("Date","Revenue")
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')   


*********************************    
 Trying to import with Pandas...   **************************************************************
  Can't get data to import.  IE-- can't the cell values to import  

import numpy as np
import pandas as pd
import csv

filename = "Desktop/python-challenge/PyBank/budget_data_1.csv"
csvpath = os.path.join('Desktop/python-challenge/PyBank', 'budget_data_1.csv')   

import pandas

data = pandas.read_csv("test.csv", header=0)
col_a = list(data.a)
col_b = list(data.b)









    
    
     