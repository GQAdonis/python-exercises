import pandas as pd
import os

def load_supply_chain_data(csv_file_path):
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
        print(f"Successfully loaded {len(df)} rows from {csv_file_path}")
        print(f"DataFrame shape: {df.shape}")
        print(f"Columns: {list(df.columns)}\n")
        return df
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")

def analyze_column_values(df, column_name, top_n=20):
    """
    Analyze value counts for a specific column.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
        column_name (str): Name of the column to analyze
        top_n (int): Number of top values to display (default: 20)
        
    Returns:
        pd.Series: Value counts for the column
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the dataset")
    
    value_counts = df[column_name].value_counts()
    
    print("="*80)
    print(f"ANALYSIS: {column_name.upper()}")
    print("="*80)
    print(f"Total unique values: {len(value_counts)}")
    print(f"Total items: {value_counts.sum()}")
    print(f"Null/Missing values: {df[column_name].isna().sum()}")
    print("\n" + "-"*80)
    print(f"{'Value':<50} {'Count':<15} {'Percentage'}")
    print("-"*80)
    
    total = value_counts.sum()
    display_counts = value_counts.head(top_n)
    
    for value, count in display_counts.items():
        percentage = (count / total) * 100
        value_str = str(value)[:47] + "..." if len(str(value)) > 50 else str(value)
        print(f"{value_str:<50} {count:<15} {percentage:>6.2f}%")
    
    if len(value_counts) > top_n:
        remaining = len(value_counts) - top_n
        print(f"\n... and {remaining} more unique values")
    
    print("-"*80)
    print(f"Most common: {value_counts.index[0]} ({value_counts.iloc[0]} occurrences)")
    print(f"Least common: {value_counts.index[-1]} ({value_counts.iloc[-1]} occurrences)")
    print("="*80)
    print("\n")
    
    return value_counts

def analyze_all_columns(df, columns_to_analyze, top_n=20):
    """
    Analyze value counts for multiple columns.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
        columns_to_analyze (list): List of column names to analyze
        top_n (int): Number of top values to display for each column
        
    Returns:
        dict: Dictionary with column names as keys and value counts as values
    """
    results = {}
    
    for column in columns_to_analyze:
        if column in df.columns:
            try:
                results[column] = analyze_column_values(df, column, top_n)
            except Exception as e:
                print(f"Error analyzing column '{column}': {str(e)}\n")
        else:
            print(f"Warning: Column '{column}' not found in dataset. Skipping...\n")
    
    return results

def generate_summary_report(results):
    """
    Generate a summary report of all analyses.
    
    Args:
        results (dict): Dictionary of analysis results
    """
    print("\n" + "="*80)
    print("SUMMARY REPORT")
    print("="*80)
    print(f"\nTotal columns analyzed: {len(results)}")
    print("\n" + "-"*80)
    print(f"{'Column':<30} {'Unique Values':<20} {'Most Common Value'}")
    print("-"*80)
    
    for column, value_counts in results.items():
        unique_count = len(value_counts)
        most_common = str(value_counts.index[0])[:30]
        most_common_count = value_counts.iloc[0]
        print(f"{column:<30} {unique_count:<20} {most_common} ({most_common_count})")
    
    print("="*80)

def save_results_to_csv(results, output_dir='analysis_results'):
    """
    Save analysis results to separate CSV files.
    
    Args:
        results (dict): Dictionary of analysis results
        output_dir (str): Directory to save result files
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for column, value_counts in results.items():
        output_file = os.path.join(output_dir, f"{column}_counts.csv")
        value_counts.to_csv(output_file, header=['Count'])
        print(f"Saved {column} analysis to: {output_file}")
    
    print(f"\nAll results saved to directory: {output_dir}")

def main():
    """
    Main function to execute the comprehensive supply chain analysis.
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
        df = load_supply_chain_data(csv_file)
        
        # Analyze all specified columns
        print(f"Analyzing {len(columns_to_analyze)} columns...\n")
        results = analyze_all_columns(df, columns_to_analyze, top_n=20)
        
        # Generate summary report
        generate_summary_report(results)
        
        # Ask if user wants to save results
        print("\n" + "="*80)
        print("Analysis complete!")
        print("="*80)
        
        # Optionally save results to CSV files
        save_choice = input("\nWould you like to save detailed results to CSV files? (yes/no): ").lower()
        if save_choice in ['yes', 'y']:
            save_results_to_csv(results)
        
        return results
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    results = main()