import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)

df = pd.read_csv('data/vgsales.csv')
print(df.info())
print(df.isnull().sum())

# Year : valeurs manquantes volontairement conservées  pour être automatiquement exclues des analyses plutôt que remplacées par une valeur arbitraire

def fill_na_publisher(df):
    return df["Publisher"].fillna("Unknown")

df = fill_na_publisher(df)
print(df.isnull().sum())