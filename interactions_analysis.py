from pathlib import Path
import pandas as pd

data_path = Path("../data")

interactions = pd.read_csv(data_path / "interactions.csv")

interactions["timestamp"] = pd.to_datetime(interactions["timestamp"])

#General information
print(interactions.head())
print("Shape:", interactions.shape)
print(interactions.describe())
print(interactions.info())

#Data quality
print(interactions.isnull().sum())
print("Duplicates:", interactions.duplicated().sum())
print("Interaction ID duplicated:", interactions["interaction_id"].duplicated().sum())

#Business metrics
print(
    interactions["interaction_type"]
    .value_counts()
)


#KPI
print("Unique users:", interactions["user_id"].nunique())
print("Unique products:", interactions["product_id"].nunique())
print("Unique sessions:", interactions["session_id"].nunique())

#dwell time
print(
    "Median dwell time:",
    interactions["dwell_time_ms"].median()
)

print(
    interactions.nlargest(
        10,
        "dwell_time_ms"
    )
)

#Temporal interval
print(
    "first interaction:",
    interactions["timestamp"].min()
)

print(
    "Last interaction:",
    interactions["timestamp"].max()
)

#Grouped
print(
    interactions.groupby(
        "interaction_type",
    )["dwell_time_ms"].mean()
    .sort_values(ascending=False)
    )

#Most active users
print(
    interactions["user_id"]
    .value_counts()
    .head(10)
)

#Most viewed products
print(
    interactions[
        interactions["interaction_type"] == "view"
    ]["product_id"]
    .value_counts()
    .head(10)
)