import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import collections
from collections import Counter

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

# Problem: stopwords such in wordcloud should be excluded (robinhood, robinhoodapp and hood) !!

#Analysis
x = []
for txt in df.iterrows():
    x += txt[1]['cleantext'].split(' ')
#Top Common Words
topwords = Counter(x).most_common()
topwords[:15]

#Visualizing the Common Words
top = topwords[:15]
top.reverse()
x , y = zip(*(top))

plt.figure(figsize=(12, 8))
plt.bar(x, y)

plt.title("Common Words Tweets mentioning Robinhood")
plt.xlabel('Ocurrences')
plt.ylabel('Words')
plt.xticks(rotation=40)
plt.show()