import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)



# Year : missing values keeped to ignore them

def fill_na_publisher(df):
    return df["Publisher"].fillna("Unknown")

# Return the top 10 sales in global
def top_sales_global(df):
    df.sort_values("Global_Sales",ascending=False)
    return df.head(10)

# Return the global Sales of each Genre, sorted
def sales_by_genres(df):
    return df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)

# Return the evolution of Global_Sales in the years
def sales_by_year(df):
    return df.groupby("Year")["Global_Sales"].sum().sort_index()

def sales_by_region_and_genre(df):
    return df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()

df = pd.read_csv('data/vgsales.csv')

df["Publisher"] = fill_na_publisher(df)

# It explain the lack of global sales since 2016, the dataset is not uploaded after this period
# We have to ignore the results since 2016
#print(df.groupby("Year")["Name"].count())

top_sales_global(df).to_csv('output/top_sales_global.csv', index=False)
sales_by_genres(df).to_csv('output/sales_by_genre.csv')
sales_by_year(df).to_csv('output/sales_by_year.csv')
sales_by_region_and_genre(df).to_csv('output/sales_by_region_and_genre.csv')