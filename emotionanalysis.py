import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from nrclex import NRCLex

#Open file cleaneddate from data
df = pd.read_csv ('./data/cleaneddate.csv', index_col=None, header=0)
df.append(df)
strdf = df['text'].to_string()

# 3 Möglichkeiten für string funktionieren nicht Fehlermeldung: must be a string, not <class 'pandas.core.series.Series'>
# strdf = df['text'].astype(str)
# strdf = pd.Series(df['text'], dtype="string")
# strdf = df['text'].str

text_object = NRCLex(strdf) # Für den String eine String-Variable strInput, besser noch binary (UNICODE-16, utf-8, utf-16) .. 

#Return words list.

text_object.words
print(text_object.words)

text_object.raw_emotion_scores
print(text_object.raw_emotion_scores)

text_object.sentences
print(text_object.sentences)

text_object.affect_list
print(text_object.affect_list)

text_object.affect_dict
print(text_object.affect_dict)

text_object.top_emotions
print(text_object.top_emotions)

text_object.affect_frequencies
print(text_object.affect_frequencies)