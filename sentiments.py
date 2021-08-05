import pandas as  pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Open file
df = pd.read_csv ('./data/cleaneddate.csv', index_col=None, header=0)
df.append(df)
df.head()

#Grouping and perform count over each group
svalue_num =  df.groupby('svaluenltk')['svaluenltk'].count()
print(svalue_num)

labels = 'Negative','Neutral','Positive'
sizes = [4075,4597,6328]
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()