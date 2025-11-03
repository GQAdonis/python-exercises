import pandas as pd

# Load the supply chain data
df = pd.read_csv('Supply Chain Data - Data.csv')

# Filter for Beauty category and China sellers
beauty_china = df[(df['Category'] == 'Beauty') & (df['SellerCountry'] == 'China')]

# Calculate sum and count of prices
sum_prices = beauty_china['Price'].sum()
count_prices = beauty_china['Price'].count()

# Display the results
print(f"Sum of Prices: {sum_prices}")
print(f"Count of Prices: {count_prices}")