import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)

df = pd.read_csv('data/vgsales.csv')
print(df.info())
print(df.isnull().sum())