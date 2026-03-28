import pandas as pd
import numpy as np

data = {
    'Name': ['Abhijit', 'Smriti', 'Akash', 'Roshni', 'Akash', None],
    'Age': [20, 19, 200, 14, 20, np.nan],
    'Category': [' Electronics ', 'Furniture', 'electronics', 'Toys', 'electronics', 'Toys'],
    'Price': ['$1,200', '$450', '$1,100', 'Free', '$1,100', '$50']
}
df = pd.DataFrame(data)
df.dropna(subset=['Name'], inplace=True) # Remove rows where 'Name' is missing
df['Age'] = df['Age'].fillna(df['Age'].median()) # Impute missing 'Age' with median
df.drop_duplicates(inplace=True)
df['Category'] = df['Category'].str.strip().str.lower()
df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').replace('Free', '0')
df['Price'] = pd.to_numeric(df['Price'])
df.loc[df['Age'] > 100, 'Age'] = 20
df.rename(columns={'Name': 'Customer_Name', 'Price': 'Price_USD'}, inplace=True)
print("Cleaned DataFrame:")
print(df)
