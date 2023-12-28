import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import plot_tree

df=pd.read_csv('balance-scale.csv')
df.head()
print(df.head())

import seaborn as sns
df.describe(include='all')
print(df['Class'].value_counts())
sns.countplot(data=df,x='Class',label='count')
