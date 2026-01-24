import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2, 3], "num_passengers": [123, 456, 789]})
df['month'] = month

print(df.head())

df.to_parquet(f"output_{month}.parquet", index=False)

print(f"Running pipeline for month {month}")