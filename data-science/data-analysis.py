import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from scipy import stats

def load_data(file_path):
    return pd.read_csv(file_path)

def compute_statistics(df):
    stats_dict = {}
    for column in df.select_dtypes(include='number'):
        stats_dict[column] = {
            'mean': df[column].mean(),
            'median': df[column].median(),
            'mode': df[column].mode().tolist()
        }
    return stats_dict

def visualize_data(df):
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols].hist(bins=20, figsize=(12, 8))
    plt.tight_layout()
    plt.show()

def main(file_path):
    df = load_data(file_path)
    stats = compute_statistics(df)

    print("\nBasic Statistics:\n")
    for col, stat in stats.items():
        print(f"{col}:")
        print(f"  Mean: {stat['mean']}")
        print(f"  Median: {stat['median']}")
        print(f"  Mode: {stat['mode']}\n")

    visualize_data(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze CSV data and plot basic stats.")
    parser.add_argument("file", help="Path to the CSV file.")
    args = parser.parse_args()
    main(args.file)
