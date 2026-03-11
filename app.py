import pandas as pd

def analyze_dataset(filepath):
    """Load and summarize a CSV dataset."""
    df = pd.read_csv(filepath)
    
    print("=== Dataset Overview ===")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n=== First 5 Rows ===")
    print(df.head())
    
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    return df

# Example usage:
# df = analyze_dataset("your_data.csv")
