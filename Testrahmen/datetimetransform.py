
#Devide date and time into two columns
import pandas as pd

#Open file
df = pd.read_csv ('./0_results_robinhood.csv', index_col=None, header=0)
df.append(df)
df.head()
df.shape
df['date']

reviews = df['date'].str.split('T',n=2,expand=True)
reviews.head()

df['dates']=reviews[0]
df['time']=reviews[1]
df.drop(columns='date',inplace=True)

reviews = df['time'].str.split('+',n=2,expand=True)
reviews.head()

df['times']=reviews[0]
df.drop(columns='1', inplace=True)

reviews = df['date'].str.split('T',n=2,expand=True)
reviews.head()

df.to_csv('./cleaneddate.csv')