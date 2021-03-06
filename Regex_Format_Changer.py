
#changes the values in the column of a dataframe

import pandas as pd
#reads the data from the csv and using regular regular expression changes the values in their right format in df
#this is part of data cleaning procedure
df = pd.read_csv('file:///C:/Users/Onotation/Documents/Internship/out.CSV')
df.values

df.AgeGroups = \
             df.AgeGroups.replace([r'^(\d{1})\_', r'_(\d{1})$'], 
                                  [r'0\1_',r'_0\1'],
                                  regex=True)
             
df.to_csv('out_changed0.csv',index = False)             
