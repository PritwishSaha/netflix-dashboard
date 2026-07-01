import pandas as pd
import numpy as np


df = pd.read_csv('netflix.csv', engine='python')

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)


print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df.drop_duplicates(inplace=True)



df['Genre'] = df['Genre'].fillna('Unknown')
df['Original_Language'] = df['Original_Language'].fillna('Unknown')


df['Release_Date'] = pd.to_datetime(df['Release_Date'])


df['Year'] = df['Release_Date'].dt.year
df['Month'] = df['Release_Date'].dt.month_name()
df['Quarter'] = df['Release_Date'].dt.quarter


df['Title'] = df['Title'].str.strip()


df['Rating_Category'] = np.where(
    df['Vote_Average'] >= 7,
    'Good',
    'Average'
)


df['Popularity_Level'] = np.select(
    [
        df['Popularity'] >= 100,
        df['Popularity'] >= 50
    ],
    [
        'High',
        'Medium'
    ],
    default='Low'
)


top_popular = (
    df[['Title', 'Popularity']]
    .sort_values('Popularity', ascending=False)
    .head(10)
)

print("\nTop 10 Popular Movies")
print(top_popular)


top_rated = (
    df[['Title', 'Vote_Average']]
    .sort_values('Vote_Average', ascending=False)
    .head(10)
)

print("\nTop 10 Rated Movies")
print(top_rated)


movies_per_year = (
    df.groupby('Year')
      .size()
      .reset_index(name='Movie_Count')
)

print("\nMovies Per Year")
print(movies_per_year.head())


genre_analysis = (
    df.groupby('Genre')
      .agg(
          Total_Movies=('Title', 'count'),
          Avg_Rating=('Vote_Average', 'mean'),
          Avg_Popularity=('Popularity', 'mean')
      )
      .reset_index()
)

print("\nGenre Analysis")
print(genre_analysis.head())


language_analysis = (
    df.groupby('Original_Language')
      .size()
      .reset_index(name='Movie_Count')
      .sort_values('Movie_Count', ascending=False)
)

print("\nLanguage Analysis")
print(language_analysis.head())


correlation = df[
    ['Popularity', 'Vote_Average', 'Vote_Count']
].corr()

print("\nCorrelation Matrix")
print(correlation)


df.to_csv('movies_cleaned.csv', index=False)


movies_per_year.to_csv(
    'movies_per_year.csv',
    index=False
)

genre_analysis.to_csv(
    'genre_analysis.csv',
    index=False
)

language_analysis.to_csv(
    'language_analysis.csv',
    index=False
)

print("\nFiles Exported Successfully!")
print("1. movies_cleaned.csv")
print("2. movies_per_year.csv")
print("3. genre_analysis.csv")
print("4. language_analysis.csv")