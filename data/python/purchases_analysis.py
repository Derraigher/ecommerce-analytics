from pathlib import Path
import pandas as pd

data_path = Path("../data")

purchases = pd.read_csv(data_path / "purchases.csv")

#date conversion
purchases['order_date'] = pd.to_datetime(purchases['order_date'])


check = purchases["quantity"] * purchases["unit_price"]
print(
    "Total amount corrected:",
    (check == purchases["total_amount"]).all()
)
#informazioni generali
print(purchases.head())
print("shape", purchases.shape)
print(purchases.info())
print(purchases.describe())


#data_quality
print(purchases.isnull().sum())
print(purchases.duplicated().sum())
print(purchases['purchase_id'].duplicated().sum())
print(purchases['quantity'].value_counts())
print("Min price:", purchases["unit_price"].min())
print("Max price:", purchases["unit_price"].max())

#business metrics
print("unique clients:", purchases["user_id"].nunique())
print("Unique products", purchases["product_id"].nunique())
print("Unique orders:", purchases["order_id"].nunique())
print("Unique purchases:", purchases["purchase_id"].nunique())
print(purchases["user_id"].value_counts().head(10))
print(
    purchases["quantity"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


print("first order:", purchases["order_date"].min())
print("last order:", purchases["order_date"].max())



#KPI
print('fatturato totale:', purchases['total_amount'].sum())
print('valore medio ordine:', purchases['total_amount'].mean())


