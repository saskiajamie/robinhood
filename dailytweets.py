import pandas as  pd

import sys

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np

# Plot a bar chart of daily number of Tweets
data = [2397,2982,1707,1818,4482,5632,34710,574026,254615,1498499,28022,27966,28397,18045,19850]
labels = ['21.01.21', '22.01.21', '23.01.21', '24.01.21', '25.01.21', '26.01.21', '27.01.21', '28.01.21',
            '29.01.21', '30.01.21', '31.01.21', '01.02.21', '02.02.21', '03.02.21', '04.02.21']
plt.xticks(range(len(data)), labels)
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets per day')
plt.bar(range(len(data)), data) 
plt.xticks(rotation=40)

plt.show()

# Plot a horizontal bar chart of daily number of Tweets
y_axis = ['21.01.21', '22.01.21', '23.01.21', '24.01.21', '25.01.21', '26.01.21', '27.01.21', '28.01.21',
            '29.01.21', '30.01.21', '31.01.21', '01.02.21', '02.02.21', '03.02.21', '04.02.21']
x_axis = [2397,2982,1707,1818,4482,5632,34710,574026,254615,1498499,28022,27966,28397,18045,19850]

plt.barh(y_axis,x_axis)
plt.title('title name')
plt.ylabel('Date')
plt.xlabel('Number of Tweets')
plt.show()
