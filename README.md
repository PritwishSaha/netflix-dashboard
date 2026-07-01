# 🎬 Netflix Movies Dashboard


![Netflix Dashboard](./Screenshot%202026-07-02%20033041.png)

## 📌 Overview
An interactive Power BI dashboard analyzing a Netflix movie dataset (~380 titles after cleaning) 
to explore trends in genre popularity, audience ratings, and release patterns over time.

## 📊 Dashboard Preview
![dashboard-demo](assets/dashboard-demo.gif)

**Key metrics at a glance:**
- 🎥 Total Movies: 387
- ⭐ Average Rating: 7.00
- 🔥 Average Popularity: 42.18
- 🗳️ Total Votes: 530K

## 🎯 Objective
- Which genres are most common and highest rated on Netflix?
- How has movie output changed over the years (spike around 2000s–present)?
- Which titles drive the most engagement (votes/popularity)?

## 🗂️ Dataset
- **Source:** TMDB/Netflix movie metadata (via Kaggle)
- **Size:** ~9,800 raw rows → cleaned to 387 relevant records
- **Fields:** Release_Date, Title, Overview, Popularity, Vote_Count, 
  Vote_Average, Original_Language, Genre, Poster_Url

## 🛠️ Tools Used
- **Excel** — initial data cleaning (removing duplicates, splitting multi-genre fields, 
  handling nulls/blank ratings, filtering by language/relevance)
- **Power BI** — data modeling, DAX measures, and dashboard visualization

## 🧹 Data Cleaning Steps (Excel / Power Query)
- Removed duplicate and irrelevant/non-Netflix titles
- Split combined `Genre` column into individual genre categories
- Converted `Release_Date` to proper date format for time-series analysis
- Handled missing `Vote_Average` / `Popularity` values
- Standardized `Original_Language` codes

## 📈 Visuals Included
| Visual | Insight |
|---|---|
| KPI Cards | Total movies, avg rating, avg popularity, total votes |
| Movies Released by Year (line chart) | Release trend, showing sharp growth post-2000 |
| Genre Pie Chart | Distribution of movies by genre |
| Movies by Genre (bar chart) | Genre volume comparison (Drama leads) |
| Highest Rated Genres (histogram) | Rating distribution, most titles rated 6–8 |
| Count of Genre by Vote_Average | Genre-rating correlation funnel |
| Title tables | Top/latest titles by genre |

## 💡 Key Insights
- Drama and Comedy dominate the catalog by volume.
- Most movies cluster around a 6–8 rating — very few outliers below 4 or above 9.
- Release volume spikes sharply after 2000, reflecting Netflix's growing content library.
- Average popularity score (42.18) suggests a long tail — a few titles drive most engagement.

## 🚀 How to Use
1. Clone this repo
2. Open `Netflix_Dashboard.pbix` in Power BI Desktop
3. If prompted, update the data source path to `netflix.csv` in this repo
4. Click **Refresh** to reload data

## 📁 Repo Structure