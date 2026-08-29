from pathlib import Path
import pandas as pd


data_path = Path("../data")
users = pd.read_csv(data_path /'users.csv')

#date conversion
users["signup_date"] = pd.to_datetime(users["signup_date"])

#General information
print(users.head())
print("Shape:", users.shape)
print(users.describe())
print(users.info())

#Data quality
print(users.isnull().sum())
print("Duplicates:", users.duplicated().sum())
print("User ID duplicates:", users["user_id"].duplicated().sum())

#Business metrics
print(users["gender"].value_counts())
print(users["loyalty_tier"].value_counts())
print(users["income_level"].value_counts())
print(users["preferred_category"].value_counts())
print("Unique countries:", users["country"].nunique())
print("Unique cities:", users["city"].nunique())
print(users["city"].value_counts().head(10))

#age analysis
users["age_group"] = pd.cut(
    users["age"],
    bins=[18, 25, 35, 45, 55, 65, 80],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65", "66+"]
)

print(users["age_group"].value_counts())

#time analysis
users["signup_year"] = users["signup_date"].dt.year
print(users["signup_year"].value_counts().sort_index())

#KPI
print("Total users:", len(users))
print("Mean age:", users["age"].mean())
print("Median age:", users["age"].median())



