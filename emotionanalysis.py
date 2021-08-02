from nrclex import NRCLex

import pandas as pd

#Open file
df = pd.read_csv ('./rbinhood.csv', index_col=None, header=0)
df.append(df)
df.head()

for i in range(len(text)):
    
    # creating objects
    emotion = NRCLex(text[i])