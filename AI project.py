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
most_review = df[['Review Count' ,'Title']].sort_values(ascending=False,
  by='Review Count').head(10)
sns.barplot(data=most_review  ,x='Review Count' ,y='Title')
plt.title('TOP 10 HIGHEST REVIEW MOVIES¶')
plt.show()
year_most_release_movie=df.groupby(['Year'])['Title'].count().sort_values(ascending=False).reset_index().head(10)
year_most_release_movie.rename({"Title":'Count movies'} ,axis=1 ,inplace=True)

sns.barplot(data=year_most_release_movie ,x='Year' ,y='Count movies')
plt.title('MOST RELEASED MOVIES IN YEAR')
plt.show()
highest_meatscore=df[['Metascore','Title']].sort_values(by='Metascore' ,ascending=False).head(25)

plt.figure(figsize=(10 , 7))
bar=sns.barplot(highest_meatscore ,x='Metascore' ,y='Title')
plt.bar_label(bar.containers[0])
plt.title('Movies with Highest Metascore')
plt.show()
