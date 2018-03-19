import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('spotifyclassification/data.csv')
train, test = train_test_split(data, test_size = 0.15)
print("Training size: {}: Test size: {}".format(len(train), len(test)))	

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']


fig = plt.figure(figsize=(12,8))
plt.title("Song Tempo Like / Deslike Distribution")
pos_tempo.hist(alpha = 0.7, bins = 30, label='positive')
neg_tempo.hist(alpha = 0.7, bins = 30, label='negative')
plt.legend(loc = 'upper right')