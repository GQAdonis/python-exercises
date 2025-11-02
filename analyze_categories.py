import pandas as pd
import os

def analyze_supply_chain_categories(csv_file_path):
    """
    Analyze supply chain data and return the number of items in each category.
    
    Args:
        csv_file_path (str): Path to the CSV file
        
    Returns:
        pd.Series: Number of items per category, sorted in descending order
    """
    # Check if file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")
    
    # Read CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(csv_file_path)
        print(f"Successfully loaded {len(df)} rows from {csv_file_path}")
        print(f"\nDataFrame shape: {df.shape}")
        print(f"Columns: {list(df.columns)}\n")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
    
    # Check if 'Category' column exists
    if 'Category' not in df.columns:
        raise ValueError("'Category' column not found in the dataset")
    
    # Count items in each category
    category_counts = df['Category'].value_counts()
    
    return category_counts

def display_category_statistics(category_counts):
    """
    Display detailed statistics about categories.
    
    Args:
        category_counts (pd.Series): Category counts from value_counts()
    """
    print("="*60)
    print("CATEGORY ANALYSIS - SUPPLY CHAIN DATA")
    print("="*60)
    print(f"\nTotal number of unique categories: {len(category_counts)}")
    print(f"Total number of items: {category_counts.sum()}")
    print("\n" + "-"*60)
    print(f"{'Category':<25} {'Count':<15} {'Percentage'}")
    print("-"*60)
    
    total = category_counts.sum()
    for category, count in category_counts.items():
        percentage = (count / total) * 100
        print(f"{category:<25} {count:<15} {percentage:>6.2f}%")
    
    print("-"*60)
    print(f"\nMost common category: {category_counts.index[0]} ({category_counts.iloc[0]} items)")
    print(f"Least common category: {category_counts.index[-1]} ({category_counts.iloc[-1]} items)")
    print("="*60)

def main():
    """
    Main function to execute the category analysis.
    """
    # Path to the CSV file
    csv_file = 'Supply Chain Data - Data.csv'
    
    try:
        # Analyze categories
        category_counts = analyze_supply_chain_categories(csv_file)
        
        # Display results
        display_category_statistics(category_counts)
        
        # Return the category counts as a dictionary for programmatic access
        print("\n\nCategory counts as dictionary:")
        category_dict = category_counts.to_dict()
        for category, count in sorted(category_dict.items()):
            print(f"  {category}: {count}")
        
        return category_counts
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    category_counts = main()