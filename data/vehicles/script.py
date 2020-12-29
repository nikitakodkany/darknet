import pandas as pd 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df = pd.read_csv('./gt_train.csv' , header=None , names = ['image' , 'category' , 'x' , 'y' , 'w' , 'h'])

print(df.head())

df['category'] = le.fit_transform(df['category'])


print(df.head(10))
