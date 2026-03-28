import pandas as pd
try:
    df = pd.read_csv('data.csv')
    print("CSV file successfully loaded into DataFrame.\n")
except FileNotFoundError:
    print("Error: The file 'data.csv' was not found.")
print("--- First 5 Rows (head) ---")
print(df.head())
print("\n--- Last 5 Rows (tail) ---")
print(df.tail())
print("\n--- DataFrame (info) ---")
df.info()
print("\n--- Statistical Summary (describe) ---")
print(df.describe())
