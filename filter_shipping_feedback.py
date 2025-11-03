import pandas as pd

# Load the supply chain data
df = pd.read_csv('Supply Chain Data - Data.csv')

# Filter data: ShippingCost <= 10 AND SellerFeedback > 95
# Sort by SellerFeedback in descending order
filtered_df = df[(df['ShippingCost'] <= 10) & (df['SellerFeedback'] > 95)].sort_values(by='SellerFeedback', ascending=False)

# Display the filtered results
filtered_df