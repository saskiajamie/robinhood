import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

#Open file
df = pd.read_csv ('./cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

#Grouping and perform count over each group
dates_num =  df.groupby('dates')['dates'].count()
print(dates_num)

# Proportion of sentiments by day
df.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Proportion of sentiments by day
sent_by_day = df.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Problem include bar chart of Tweet number per day + x axis should include every day !!

# Plot a line graph of daily sentiments
p1 = sent_by_day.plot(stacked = False, figsize=(10,7),
                           color = ['red', 'goldenrod', 'green'], alpha = 1, fontsize=12)

p1.set_title('Tweet Sentiment Distribution Over Time', fontsize=12, pad=12)
p1.set_xlabel('Date', fontsize=12)
p1.set_ylabel('Sentiment (%)', fontsize=12, labelpad=12)
p1.legend(['Negative', 'Neutral', 'Positive'], facecolor='white', framealpha=1, fontsize=12)
plt.xticks(rotation=40)

plt.show()



