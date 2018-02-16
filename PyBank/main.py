# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:42:30 2018

@author: Adam Knapp
"""

    row_count = len(data)
    
import csv
import os   

csvpath = os.path.join('Desktop\python-challenge\PyBank', 'budget_data_1.csv')




import CSV
With open(‘budget_data_1.csv’, ‘rb’) as f:
reader = csv.reader(f)
for row in reader:
print row


***********************************************************************

# importing csv module
import csv
 
# csv file name
filename = "aapl.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = csvreader.next()
 
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