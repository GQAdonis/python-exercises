import pandas as pd

# Load the supply chain data
df = pd.read_csv('Supply Chain Data - Data.csv')

# Calculate total quantity sold for Home Improvement category
total_quantity = df[df['Category'] == 'Home Improvement']['Quantity'].sum()

# Display the result
total_quantity