import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Pie chart of positive and negative words overall the cleantext
# Numbers taken from Jupyter Notebook Code as follows:
   #import nltk
   #from nltk.sentiment.vader import SentimentIntensityAnalyzer
   #import warnings
   #warnings.filterwarnings("ignore")
   #Sentiment Analysis
   #def fetch_sentiment_using_SIA(text):
     #sid = SentimentIntensityAnalyzer()
     #polarity = sid.polarity_scores(text)
     #return 'neg' if polarity['neg'] > polarity['pos'] else 'pos'

   #sentiments_using_SIA = df.cleantext.apply(lambda text: fetch_sentiment_using_SIA(text))

   #sp = pd.DataFrame(sentiments_using_SIA.value_counts())
   #sp

labels = 'Positive Words','Negative Words'
sizes = [10956, 4044]
explode = (0.1, 0) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()