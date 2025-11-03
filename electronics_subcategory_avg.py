import pandas as pd

# Load the supply chain data
df = pd.read_csv('Supply Chain Data - Data.csv')

# Filter for Electronics category and calculate average price by subcategory
avg_price_by_subcategory = df[df['Category'] == 'Electronics'].groupby('SubCategory')['Price'].mean()

# Display the results
avg_price_by_subcategory