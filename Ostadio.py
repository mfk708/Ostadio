# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:51:51 2020

@author: moham
"""
import pandas as pd
import numpy as np
df = pd.read_csv('ostadio_march_30_2020.csv', index_col='Day')
pd.set_option('display.max_columns', 85)
df
df.info()
df.head()
df.columns
df.shape
df.index
df['Date']
df['Page view']
df['Referral']
df['Weekdays']
df['Weekdays'].value_counts()
df["Weekdays"].replace('saturday', 'Saturday', inplace=True) #replace all 'saturday's with 'Saturday'.
df.loc[3]
df.iloc[[],3]
df['Users'].value_counts().head(50)
week_days=['saturday', 'Sunday', 'Monday']
filt = df['Weekdays'].isin(week_days) 
df[filt].head(50)
df.loc[filt, 'Users']
filt_sat= df['Weekdays'] == 'saturday'
df.loc[filt_sat, 'Users'].mean()
df.sort_values('Users', ascending=False)
df.nlargest(10, 'Users' )
df.nsmallest(10, 'Users')
df['Users'].median()
weekday_grp= df.groupby('Weekdays') #creates grouping based on 'weekdays'.
weekday_grp.get_group('Saturday')
weekday_grp['Users'].mean()
eekday_grp['Users', 'Session'].agg(['median', 'mean'])
weekday_grp['Users', 'Session'].agg(['median', 'mean']).sort_values(by=('Users', 'mean'))
listall = ['Users', 'New users', 'Returning users', 'Page view', 'Bounce Rate','Session','organic search', 'Direct search', 'Alexa']
weekday_grp[listall].agg(['median', 'mean']).sort_values(by=('Users', 'mean'), ascending=False)
df['Users'] = df['Users'].astype(float)
df[' New users'] = df['New users'].astype(float)
df['newuser_user']= (df['New users']/df['Users'])newratio
df['New users'].dtype
weekday_grp['newuser_user'].agg(['median', 'mean']).sort_values(by='median')
df.describe()
df["Date"].head(100)
df['Date'] =pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')
df['Date'] = pd.to_datetime(df['Date'], format ='%m-%d-%Y')
df['Date'].dtype
df['Date'].shape
df['Date', 2]
df['Date'].value_counts()
df.index
df['Date'].loc[[1,2,3,4]]
a=[1,2,3,...,305]
a=range(1,304)
b= range (300, 305)
df['Date'].str.split('/', expand = True)
df["Date"]
#date formats are different in the file. so I split the ones with '/' from '/', create three different columns of day, month, and year. then put them back together in the desired format.
df[['month', 'day', 'year']] = df['Date'].str.split('/', expand = True)
#df[['month', 'day', 'year']] = df['Date'].str.split('-', expand = True)
df['day']
for x in range(1,305):
    if (df.loc[x,'day']) != 'None':
        df['Tarikh'] = df['day'] + '-' + df['month'] + '-' + df['year']
    else:
        df.loc[x,'Tarikh'] = df.loc[x,'Date']
df['Tarikh']   
for x in range(1, 92):
    df.loc[x,'Tarikh'] = df.loc[x,'Date']  
    
df.drop(columns=['Tari', 'Tarik'], inplace=True)
df['Date'] 
df['Tarikh']   
df['Users'].max()   
df['Users'].min()
bins = np.linspace(min(df['Users']), max(df['Users']), 4) #creates 3 bins for the 'Users' column.
group_names = ["low_traffic", 'Average traffic', 'High traffic']
df['Users_binned'] = pd.cut(df['Users'], bins, labels=group_names, include_lowest=True)
pd.get_dummies(df['day-on-off']) #using one-hot coding creates dummy variables for a categorical variable.
