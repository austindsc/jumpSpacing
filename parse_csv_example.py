import csv
import pandas as pd

# Method 1: Using csv module (handles newlines in quoted fields automatically)
def parse_with_csv_module(filepath):
    """Parse CSV with multi-line headers using csv module"""
    with open(filepath, 'r', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Get headers
        data = list(reader)     # Get all data rows
    
    print("Headers:")
    for i, header in enumerate(headers):
        # Replace newlines with spaces for display
        clean_header = header.replace('\n', ' ')
        print(f"  Column {i}: {clean_header}")
    
    return headers, data


# Method 2: Using pandas (recommended - most convenient)
def parse_with_pandas(filepath):
    """Parse CSV with multi-line headers using pandas"""
    # Pandas handles multi-line headers automatically
    df = pd.read_csv(filepath)
    
    # Optional: Clean up column names by replacing newlines with spaces
    df.columns = [col.replace('\n', ' ').strip() for col in df.columns]
    
    return df


# Example usage
if __name__ == "__main__":
    filepath = "data/fp.csv"
    
    print("=" * 60)
    print("Method 1: Using csv module")
    print("=" * 60)
    headers, data = parse_with_csv_module(filepath)
    print(f"\nFound {len(headers)} columns and {len(data)} rows")
    
    print("\n" + "=" * 60)
    print("Method 2: Using pandas (recommended)")
    print("=" * 60)
    df = parse_with_pandas(filepath)
    print(f"\nDataFrame shape: {df.shape}")
    print("\nColumn names:")
    for col in df.columns:
        print(f"  - {col}")
    
    print("\nFirst few rows:")
    print(df.head())
    
    # You can now work with the dataframe normally
    print("\nExample: Accessing 'gap (cm)' column:")
    print(df['gap (cm)'].head())
