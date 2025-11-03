import pandas as pd

# Load the supply chain data
df = pd.read_csv('Supply Chain Data - Data.csv')

# Calculate average shipping cost for Outdoors category
average_shipping = df[df['Category'] == 'Outdoors']['ShippingCost'].mean()

# Display the result
average_shipping