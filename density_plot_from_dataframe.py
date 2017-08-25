
#Density Plot Creater

import matplotlib.pyplot as plt
import pandas as pd
#creates density plot out of dataframe

import numpy as np
plt.style.use('fivethirtyeight')

df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv')
df.values
print df
counts = df.groupby(['Age','Gender']).count()


meanAge = df.ix[:,1:].mean()
print meanAge

sdAge = df.ix[:,1:].std()
print sdAge


df1 = (df.ix[:,1:] - df.ix[:,1:].mean()) / df.ix[:,1:].std()
df1['Gender'] = df['Gender']
print df1

counts1 = df1.groupby(['Age']).count()
#print counts1
   
ax1 = df1.plot(kind='kde', figsize=(10, 6))
arr = ax1.get_children()[0]._x

plt.xticks(np.linspace(arr[0], arr[-1]), rotation=45)
plt.ylabel('Density Of Cocktails',fontsize=20)
plt.title('Distribution Of Z Scores Of Ages By Density Of Cocktails',fontsize=40)
plt.xlabel('Z Scores')
   

plt.show()  

