Data Analysis Script

This script (data-analysis.py) performs basic data analysis on a CSV file. It loads your dataset, computes key statistics (mean, median, mode), and visualizes distributions using Matplotlib.

📊 Features

Load CSV files with numeric columns

Compute basic statistics:

Mean

Median

Mode

Generate histograms for visual analysis

🧰 Requirements

Install dependencies before running:

pip install pandas matplotlib seaborn scipy


If you’re on Linux and plots don’t display:

sudo apt install python3-tk

🚀 Usage

Run the script from the command line:

python3 data-analysis.py example-data.csv

Example Output
Basic Statistics:

height:
  Mean: 170.5
  Median: 170.0
  Mode: [172.0]

weight:
  Mean: 70.2
  Median: 69.5
  Mode: [68.0]


The script will also display histograms for each numeric column.

📁 Example Data

example-data.csv is provided as a sample dataset containing numeric columns (e.g., height, weight, age) for testing.
