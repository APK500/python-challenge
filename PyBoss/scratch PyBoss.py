# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:24:23 2018

@author: Adam Knapp
"""
#IMPORTING THE FILE****   

import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')

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
    
    
    
    ***************************splitting the name column*****
    
    
import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')

import csv
with open(csvpath, newline='') as csvfile:

    with open('Desktop/python-challenge/PyBoss/employee_data1New.csv', 'r') as f:
        data = list(csv.reader(f))
        
        NO RESULTS*******************************************
        

import os

def split(filehandler, delimiter=',', row_limit=10000, 
    output_name_template='employee_data1New.csv', output_path='Desktop/python-challenge/PyBoss.', keep_headers=True):
    """
    Splits a CSV file into multiple pieces.
    
    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file.
    Example usage:
    
        >> from toolbox import csv_splitter;
        >> csv_splitter.split(open('/home/ben/input.csv', 'r'));
    
    """
def split(filehandler, delimiter=',', row_limit=10000,
output_name_template='employee_data1New.csv', output_path='.', keep_headers=True):
    
    
    
    
 ****************************************************   
    
    
import sys,os
import py2 as csv
import converter,iohelper
from itertools import groupby

def do_split(csvfilepath,colidx):
    result = {}
    header=[]
    iohelper.delete_file_folder('splitted/')
    iohelper.dir_create('splitted/')
    with open(csvfilepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, encoding='utf-8')
        header=csvreader.next()
        for row in csvreader:
            if row[colidx] in result:
                result[row[colidx]].append(row)
                if(len(result[row[colidx]])>100000):
                    print ('start---%s' % row[colidx])
                    with open("splitted/%s.csv" % row[colidx], "ab") as output:
                        wr = csv.writer(output, encoding='utf-8')
                        if os.path.getsize("splitted/%s.csv" % row[colidx])==0:
                            wr.writerow(header)
                            converter.convert_to_utf8("splitted/%s.csv" % row[colidx])
                        for line in result[row[colidx]]:
                            wr.writerow(line)
                        print ('end---%s' %row[colidx])
                    result[row[colidx]]=[]
            else:
                result[row[colidx]] = [row]
        for attr, value in result.iteritems():
            if attr!='-' and attr!='':
                print ('start---%s' %attr)
                with open("splitted/%s.csv" %attr, "ab") as output:
                    wr = csv.writer(output, quoting=csv.QUOTE_ALL)
                    if os.path.getsize("splitted/%s.csv" % attr)==0:
                        wr.writerow(header)
                        converter.convert_to_utf8("splitted/%s.csv" % attr)
                    for line in value:
                        wr.writerow(line)
                    print ('end---%s' %attr)
                value=[]
                
**********************************************
import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')

import csv
with open(csvpath, newline='') as csvfile:

    
    with open('Desktop/python-challenge/PyBoss/employee_data1.csv') as inf:
        with open('Desktop/python-challenge/PyBoss/employee_data1New.csv', 'w') as outf:
            for line in inf:
                outf.write(','.join(line.split('\\')))  
                
                
    *************************************
import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')

import csv
with open(csvpath, newline='') as csvfile:    
    
    reader = csv.reader(scsv.split('\n'), delimiter=',')
    for row in reader:
        print('\t'.join(row))
        
 *****************************************
       
import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')

import csv
with open(csvpath, newline='') as csvfile:   


    from io import StringIO
import csv

scsv = """text"""

f = StringIO(scsv)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print('\t'.join(row))
    
*************

import pandas as pd
import numpy as np

import os
csvpath = os.path.join('Desktop/python-challenge/PyBoss', 'employee_data1.csv')
import csv
with open(csvpath, newline='') as csvfile:
    
    pd.read_csv("Desktop/python-challenge/PyBoss/employee_data1.csv")
    
    df.count()


    
    
import pandas as pd 

d = {'name': ['Braund', 'Cummings', 'Heikkinen', 'Allen'],
     'age': [22,38,26,35],
     'fare': [7.25, 71.83, 0 , 8.05], 
     'survived?': [False, True, True, False]}

df = pd.DataFrame(d)

print(df)    
    
    