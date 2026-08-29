from pathlib import Path
import pandas as pd

data_path = Path("../data")

products = pd.read_csv(data_path / "products.csv")

products['date_added'] = pd.to_datetime(products['date_added'])

#General information
print(products.head())
print("Shape:", products.shape)
print(products.describe())
print(products.info())

#Data quality
print(products.isnull().sum())
print("Duplicates:", products.duplicated().sum())
print("Product ID duplicates:", products["product_id"].duplicated().sum())

#Business metrics
print(products["category"].value_counts())
print(products["brand"].value_counts())
print(products["stock_quantity"].value_counts())

#KPI
print("Total products:", len(products))
print("Unique categories:", products["category"].nunique())
print("Unique subcategories:", products["subcategory"].nunique())
print("Unique brands:", products["brand"].nunique())

#Price analysis
print("Average price:", products["price"].mean())
print("Median price:", products["price"].median())
print("Min price:", products["price"].min())
print("Max price:", products["price"].max())

#Most expensive products
print(
    products.nlargest(
        10,
        "price"
    )[["product_name", "brand", "price"]]
    )
#Stock analysis
print("Average stock:", products["stock_quantity"].mean())
print("Median stock:", products["stock_quantity"].median())
print("Max stock:", products["stock_quantity"].max())
#Top stock
print(
    products.nlargest(
        10,
        "stock_quantity"
    )[["product_name", "stock_quantity"]]
)

#Rating analysis
print(
    "products with ratings:",
    products["rating_avg"].notnull().sum()
)

print(
    "Products without rating:",
    products["rating_avg"].isnull().sum()
)

print(products["rating_avg"].describe())
print(
    products.nlargest(
    10,
     "rating_avg"
    )[["product_name", "rating_avg", "review_count"]]
)

#temporal analysis
print("First products:", products["date_added"].min())
print("Last product:", products["date_added"].max())

products["year_added"] = products["date_added"].dt.year

print(
    products["year_added"]
    .value_counts()
    .sort_index()
)

print(
    products.groupby("category")["price"]
    .mean()
    .sort_values(ascending=False)
)

print(
    products.groupby("category")
    .size()
    .sort_values(ascending=False)
)

print(
    products.groupby("category")["rating_avg"]
    .mean()
    .sort_values(ascending=False)
)



