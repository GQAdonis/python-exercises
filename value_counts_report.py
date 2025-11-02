import pandas as pd
import os

def load_data(csv_file_path):
    """
    Load supply chain data from CSV file.
    
    Args:
        csv_file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")
    
    try:
        df = pd.read_csv(csv_file_path)
        print(f"Successfully loaded {len(df)} rows from {csv_file_path}\n")
        return df
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")

def display_value_counts(df, column_name):
    """
    Display value counts for a column in ascending order.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
        column_name (str): Name of the column to analyze
    """
    if column_name not in df.columns:
        print(f"Warning: Column '{column_name}' not found in dataset. Skipping...\n")
        return
    
    print(f"# Getting value counts from the column")
    print(f"df['{column_name}'].value_counts(ascending=True)")
    print()
    
    # Get value counts in ascending order
    value_counts = df[column_name].value_counts(ascending=True)
    
    # Display as DataFrame to match the screenshot format
    result_df = pd.DataFrame({column_name: value_counts.index, 'count': value_counts.values})
    result_df.set_index(column_name, inplace=True)
    
    print(result_df)
    print()
    print("="*80)
    print()

def main():
    """
    Main function to display value counts for all specified columns.
    """
    # Path to the CSV file
    csv_file = 'Supply Chain Data - Data.csv'
    
    # Columns to analyze
    columns_to_analyze = [
        'Category',
        'SubCategory',
        'ProductName',
        'Description',
        'SellerName',
        'SellerCountry',
        'OrderStatus',
        'OrderDate'
    ]
    
    try:
        # Load data
        df = load_data(csv_file)
        
        # Display value counts for each column
        for column in columns_to_analyze:
            display_value_counts(df, column)
        
        print("Analysis complete!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()