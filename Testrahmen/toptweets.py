import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Open file
df = pd.read_csv ('Testrahmen/cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()


# Create dataframe of top twenty tweets per day by likes
top_20_by_day = []
for i in df.groupby('dates')['likes'].nlargest(20).index:
    top_20_by_day.append(i[1])
    
top_20_by_day = df.loc[top_20_by_day]
top_20_by_day.shape


# Proportion of sentiments of top twenty tweets by day
sent_top_20_by_day = top_20_by_day.groupby('dates')['svaluenltk'].value_counts(normalize=True).unstack()

# Plot a stacked line graph
p1 = sent_top_20_by_day.plot.area(stacked = True, figsize=(15,8),
                           color = ['red', 'goldenrod', 'green'], alpha = .70, fontsize=12)

p1.set_title('Sentiment of Daily Top Twenty Tweets', fontsize=12, pad=10)
p1.set_xlabel('Date', fontsize=12)
p1.set_ylabel('Sentiment (%)', fontsize=12, labelpad=10)
plt.setp(p1.get_xticklabels(), fontsize=12)
plt.setp(p1.get_yticklabels(), fontsize=12)
p1.legend(['Negative', 'Neutral', 'Positive'], facecolor='white', framealpha=1, fontsize=25)

# p1.show()

# Create dataframes for positive, neutral and negative sentiment
positive_df = df[df['svaluenltk'] == 'positive']
neutral_df = df[df['svaluenltk'] == 'neutral']
negative_df = df[df['svaluenltk'] == 'negative']

positive_df.shape, neutral_df.shape, negative_df.shape

df['svaluenltk'].value_counts()

