import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from scipy import stats

def load_data(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"\n✅ Successfully loaded data from {file_path}")
        print(f"📊 Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        exit(1)
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        exit(1)


def compute_statistics(df):
    """
    Compute mean, median, and mode for each numeric column.
    """
    stats_dict = {}
    for column in df.select_dtypes(include="number"):
        stats_dict[column] = {
            "mean": round(df[column].mean(), 2),
            "median": round(df[column].median(), 2),
            "mode": df[column].mode().tolist()
        }
    return stats_dict


def compute_group_statistics(df):
    """
    Compute average of numeric columns grouped by the first categorical column.
    Example: Average Salary per Department.
    """
    cat_cols = df.select_dtypes(exclude="number").columns
    if len(cat_cols) == 0:
        return None
    group_col = cat_cols[0]
    grouped = df.groupby(group_col).mean(numeric_only=True).round(2)
    return group_col, grouped


def visualize_data(df):
    """
    Create histograms for all numeric columns.
    """
    sns.set(style="whitegrid")
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols].hist(bins=15, figsize=(12, 8), color="#69b3a2", edgecolor="black")
    plt.suptitle("Distributions of Numeric Features", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


def main(file_path):
    """
    Main function: load data, compute stats, display results, and visualize.
    """
    df = load_data(file_path)
    stats = compute_statistics(df)

    print("\n📈 Basic Statistics:\n")
    for col, stat in stats.items():
        print(f"{col}:")
        print(f"  Mean: {stat['mean']}")
        print(f"  Median: {stat['median']}")
        print(f"  Mode: {stat['mode']}\n")

    # Optional per-group averages
    group_result = compute_group_statistics(df)
    if group_result:
        group_col, grouped = group_result
        print(f"\n🏢 Average Values per {group_col}:\n")
        print(grouped.to_string(index=True))
        print()

    visualize_data(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze CSV data and plot basic statistics.")
    parser.add_argument("file", help="Path to the CSV file.")
    args = parser.parse_args()
    main(args.file)

