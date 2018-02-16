# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:42:30 2018

@author: Adam Knapp
"""
#*********************************************************************
    row_count = len(data)
    
import csv
import os   

csvpath = os.path.join('Desktop\python-challenge\PyBank', 'budget_data_1.csv')




import CSV
With open(‘budget_data_1.csv’, ‘rb’) as f:
reader = csv.reader(f)
for row in reader:
print row


#*******************************************************************


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
    