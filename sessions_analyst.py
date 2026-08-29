from pathlib import Path
import pandas as pd

data_path = Path("../data")

sessions = pd.read_csv(data_path / "sessions.csv")

sessions["start_time"] = pd.to_datetime(sessions["start_time"])

#General information
print(sessions.head())
print("Shape:", sessions.shape)
print(sessions.describe())
print(sessions.info())

#Data quality
print(sessions.isnull().sum())
print("Duplicates:", sessions.duplicated().sum())
print("Session ID duplicates:", sessions["session_id"].duplicated().sum())


#Business metrics
print(sessions["device_type"].value_counts())
print(sessions["referrer_source"].value_counts())

#KPI
print("Unique users:", sessions["user_id"].nunique())
print("Total sessions:", len(sessions))

print(
    sessions["is_converted"]
    .value_counts()
)

conversion_rate = (
    sessions["is_converted"]
    .mean()
    *100
)

print(
    "conversion_rate",
    round(conversion_rate, 2),
    "%"
)

#Grouping
print(
    sessions.groupby(
        "device_type"
    )["is_converted"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

print(
    sessions.groupby(
        "referrer_source"
    )["is_converted"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

#Time analysis
print(
    "First session:",
    sessions["start_time"].min()
)

print(
    "Last session:",
    sessions["start_time"].max()
)