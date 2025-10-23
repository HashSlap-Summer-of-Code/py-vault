# 📊 Data Analysis Script

This script (`data-analysis.py`) performs **basic data analysis** on CSV files.  
It loads data, computes summary statistics (mean, median, mode), and visualizes numeric columns using **Matplotlib**.

---

## 🚀 Features
✅ Load CSV files  
✅ Compute:
- Mean  
- Median  
- Mode  

✅ Visualize numeric columns with histograms  

---

## 🧰 Requirements
Install dependencies:

```bash
pip install pandas matplotlib seaborn scipy
```
If plots don’t appear on Linux:
```bash
sudo apt install python3-tk
```
💻 Usage

Run the script from your project directory:
```bash
python3 data-analysis.py example-data.csv
```
📁 Example Data

example-data.csv includes 10 employees with details such as Age, Experience (Years), Salary, and Performance Score.

📈 Example Output
```yaml
📈 Basic Statistics:

Age:
  Mean: 33.1
  Median: 31.5
  Mode: [25, 27, 28, 29, 30, 33, 35, 38, 41, 45]

Experience_Years:
  Mean: 7.2
  Median: 6.5
  Mode: [2, 3, 4, 5, 6, 7, 8, 10, 12, 15]

Salary:
  Mean: 65100.0
  Median: 64500.0
  Mode: [58000, 60000, 61000, 62000, 64000, 65000, 68000, 70000, 71000, 72000]

Performance_Score:
  Mean: 82.1
  Median: 82.5
  Mode: [70, 73, 76, 78, 80, 85, 88, 89, 90, 92]
```
![Example Histogram](https://github.com/FionaG26/py-vault/blob/feature/data-analysis-script/data-science/Figure_1.png?raw=true)

🧑‍💻 Author

Developed by [FionaG26](https://github.com/FionaG26)

as part of HashSlap Summer of Code — Issue #13 (Add a Data Analysis Script)
