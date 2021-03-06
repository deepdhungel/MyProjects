
#Risk Ratio Calculation 

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 19:20:20 2017

@author: OnoTation
"""


#import the library
import pandas as pd


#read the csv as df 
df = pd.read_csv('file:///C:/Users/OnoTation/Desktop/Internship/tableforpython.csv')
df.values

#assemlbe unique age groups 
ages= df.AgeGroups.unique()

#group the dataframes by agegroup, factor and cancer and calculate the frequency distribution 
grp = df.groupby(['AgeGroups','Factor','Cancer']).Frequency.sum()

counts = grp.unstack(level=[2])

#risk with or without cancer 
counts['sumwwoCancer']= counts['No']+counts['Yes']

test = counts['cumInci']=((counts['Yes']/counts['sumwwoCancer'])*100)
test1 = test.unstack(level=[1])

#RR,ARP,PF calculation 
test1['RR'] = (test1['w-statin']/test1['wo-statin'])
test1['ARP']= (test1['RR']-1/test1['RR'])

test1['PF']= (1-test1['RR'])

print test1
