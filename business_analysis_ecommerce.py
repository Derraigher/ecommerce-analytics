from pathlib import Path
import pandas as pd

data_path = Path("../data")

users = pd.read_csv(data_path / "users.csv")
products = pd.read_csv(data_path / "products.csv")
purchases = pd.read_csv(data_path / "purchases.csv")
reviews= pd.read_csv(data_path / "reviews.csv")
sessions = pd.read_csv(data_path / "sessions.csv")
interactions = pd.read_csv(data_path / "interactions.csv")

merged = purchases.merge(
    users,
    on="user_id"
)


# =====================================
# BUSINESS ANALYSIS
# =====================================


print(
merged.groupby(
    "loyalty_tier"
)["total_amount"] \
    .mean() \
    .sort_values(ascending=False))

print(
merged.groupby(
    "loyalty_tier"
)["total_amount"] \
    .sum() \
    .sort_values(ascending=False))

print(
    merged.groupby("loyalty_tier").agg({"total_amount" : ["mean", "sum", "count"]})
)


print(
merged.groupby(
    "income_level"
)["total_amount"] \
    .mean() \
    .sort_values(ascending=False))

print(
merged.groupby(
    "income_level"
)["total_amount"] \
    .sum() \
    .sort_values(ascending=False))

print("Medium age:",merged["age"].mean())

print(
merged.groupby(
    "country"
)["total_amount"] \
    .sum() \
    .sort_values(ascending=False))

#Products

merged = merged.merge(
    products,
    on="product_id"
)

print(
merged.groupby(
    "category"
)["total_amount"] \
    .sum() \
    .sort_values(ascending=False))

print(
    merged.groupby("category").agg({"total_amount" : ["mean", "sum"],
    "quantity" :  "sum"
                                    })
.sort_values(("total_amount", "sum"),
             ascending=False)
)


print(
merged.groupby(
    "brand"
)["total_amount"] .sum() .sort_values(ascending=False))

print(
merged.groupby(
    "category"
)["price"] \
    .mean() \
    .sort_values(ascending=False))

#Reviews
reviews_products = reviews.merge(
    products,
    on="product_id"
)

print(
reviews_products.groupby(
    "brand"
)["rating"] \
    .mean() \
    .sort_values(ascending=False))

brand_rating = reviews_products.groupby("brand").agg(
    {"rating": ["mean", "count"]}
)

print(brand_rating.sort_values(
    ("rating", "count"), ascending=False))
#Sessions

print(
sessions.groupby(
    "device_type"
)["is_converted"] \
    .mean() * 100)

print(
sessions.groupby(
    "referrer_source"
)["is_converted"] \
    .mean() * 100)

#Top 10 products for earnings
print(
    merged.groupby("product_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

#Top 10 products for selling quantity
print(
    merged.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

#Average rating for category
print(
    reviews_products.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
)

#Rating-selling relation

sales = merged.groupby("product_id")["total_amount"].sum()

ratings = reviews.groupby("product_id")["rating"].mean()

comparison = pd.concat([sales, ratings], axis=1)

print(comparison.head())

comparison = comparison.dropna()

print(
    comparison["total_amount"]
    .corr(comparison["rating"])
)


