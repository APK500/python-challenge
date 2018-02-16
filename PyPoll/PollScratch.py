# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:45:54 2018

@author: Adam Knapp
"""


*****ALT code found on Geek to find sums****


with open(adresse,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    
    *******************
    
*****************************************************

    
METHOD 1 PULLING IN CSV ROWS    
# METHOD 1 OF PULLING IN CSV ROWS 
    
import os
csvpath = os.path.join('Desktop/python-challenge/PyPoll', 'election_data_1.csv')


# # Method 1: Plain Reading of CSVs
with open(csvpath, 'r') as file_handler:
   lines = file_handler.read()
   print(lines)
   print(type(lines))
    
 

 ****************************************************************   
    
BEST METHOD FOR HW-- PULLING IN CSV AND PRINTING DATA AND ROWS!!    
 
import os
csvpath = os.path.join('Desktop/python-challenge/PyPoll', 'election_data_1.csv')

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
    
    
    ***********************************************************
    
import csv
import os

# Specify the file to write to
output_path = os.path.join('Desktop/python-challenge/PyPoll', 'new.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
    
    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    
    
