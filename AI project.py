# Data analysis library
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
 
    
# Data visualization library
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        df=pd.read_csv("/kaggle/input/imdb-movies-data/imdb-movies-dataset.csv")
df.head(2)
df.dtypes
df.dropna(inplace=True) 
  df['Review Count']=df['Review Count'].str.replace(',','').astype(int)
df['Votes']=df['Votes'].str.replace(',','').astype(int)
df['Year']=df['Year'].astype(int)

top_rating=df[['Rating','Title']].sort_values(ascending=False ,by='Rating').head(10)
sns.barplot(data=top_rating,y='Title' ,x='Rating' )
plt.title('TOP 10 RATING MOVIES')
plt.show()
top_votes=df[['Votes','Title']].sort_values(ascending=False, by='Votes').head(10)

sns.barplot(data=top_votes  ,x='Votes' ,y='Title')
plt.title('TOP 10 HIGHEST VOTES MOVIES')
plt.show()