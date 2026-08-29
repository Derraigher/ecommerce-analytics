from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

data_path = Path("../data")

engine = create_engine(
    "mysql+pymysql://root:0000@localhost/ecommerce_project"
)

tables = [
    "users",
    "products",
    "purchases",
    "reviews",
    "sessions",
    "interactions"
]

for table in tables:
    df = pd.read_csv(data_path / f"{table}.csv")
    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )
    print(f"{table} loaded")