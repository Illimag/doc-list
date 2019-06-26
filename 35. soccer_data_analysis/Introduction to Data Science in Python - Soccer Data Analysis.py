import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from customplot import *
# Create your connection.
cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)

df.columns

df.describe().transpose()

#is any row NULL ?
df.isnull().any().any(), df.shape

df.isnull().sum(axis=0)

# Take initial # of rows
rows = df.shape[0]

# Drop the NULL rows
df = df.dropna()

#print(rows)
df.isnull().any().any(), df.shape

rows - df.shape[0]

df = df.reindex(np.random.permutation(df.index))

df.head(5)

df[:10][['penalties', 'overall_rating']]

df['overall_rating'].corr(df['penalties'])

potentialFeatures = ['acceleration', 'curve', 'free_kick_accuracy', 'ball_control', 'shot_power', 'stamina']

for f in potentialFeatures:
    related = df['overall_rating'].corr(df[f])
    print("%s: %f" % (f,related))

cols = ['potential',  'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']

correlations = [ df['overall_rating'].corr(df[f]) for f in cols ]

len(cols), len(correlations)

def plot_dataframe(df, y_label):  
    color='coral'
    fig = plt.gcf()
    fig.set_size_inches(20, 12)
    plt.ylabel(y_label)

    ax = df.correlation.plot(linewidth=3.3, color=color)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.attributes, rotation=75); #Notice the ; (remove it and see what happens !)
    plt.show()

df2 = pd.DataFrame({'attributes': cols, 'correlation': correlations}) 

plot_dataframe(df2, 'Player\'s Overall Rating')




# Define the features you want to use for grouping players

select5features = ['gk_kicking', 'potential', 'marking', 'interceptions', 'standing_tackle']