# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:42:30 2018

@author: Adam Knapp
"""
#Import the File
import csv
import os
import pandas as pd
import numpy as np


csvpath = os.path.join('Desktop\python-challenge\PyBank', 'budget_data_1.csv')
row_count = sum(1 for row in csv)
print(row_count)





import csv
import os

csvpath = os.path.join('Desktop\python-challenge\PyBank', 'budget_data_1.csv')
print(row_count)



with open('Desktop\python-challenge\PyBank',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    
import csv
import os   

csvpath = os.path.join('Desktop\python-challenge\PyBank', 'budget_data_1.csv')




