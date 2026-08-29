from pathlib import Path
import pandas as pd

data_path = Path("../data")

reviews = pd.read_csv(data_path / "reviews.csv")

reviews["review_date"] = pd.to_datetime(reviews["review_date"])

#General information
print(reviews.head())
print("Shape:", reviews.shape)
print(reviews.describe())
print(reviews.info())
print(reviews["rating"].value_counts().sort_index())

#Data quality
print(reviews.isnull().sum())
print("Duplicates:", reviews.duplicated().sum())
print("Review ID duplicates:", reviews["review_id"].duplicated().sum())

#Business metrics
print(reviews["review_id"].value_counts())
print(reviews["review_id"].value_counts())

#KPI
print("Total reviews:", len(reviews))
print("Unique users:", reviews["user_id"].nunique())
print("Unique products:", reviews["product_id"].nunique())

#Temporal analysis
print("First review:", reviews["review_date"].min())
print("Last review:", reviews["review_date"].max())

#Users analysis
print(
    reviews["user_id"]
    .value_counts()
    .head(10)
)
#Products analysis
print(
    reviews["product_id"]
    .value_counts()
    .head(10)
)

#group rating
print(
    reviews.groupby("product_id")["rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)