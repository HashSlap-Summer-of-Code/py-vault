# 🤖 Machine Learning Classifier

> A comprehensive machine learning classifier implementation using scikit-learn with the Iris dataset

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## 🔍 About

This project demonstrates a complete machine learning pipeline using the famous Iris flower dataset. The classifier compares multiple algorithms including Random Forest, Logistic Regression, and Support Vector Machine to predict flower species based on their physical characteristics.

The Iris dataset contains 150 samples of iris flowers with 4 features:
- Sepal length
- Sepal width
- Petal length
- Petal width

The goal is to classify flowers into one of three species:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

## ✨ Features

- **Multiple ML Algorithms**: Compare Random Forest, Logistic Regression, and SVM
- **Data Exploration**: Comprehensive exploratory data analysis
- **Data Visualization**: Beautiful plots and charts using matplotlib and seaborn
- **Model Evaluation**: Cross-validation, accuracy metrics, and confusion matrices
- **Clean Code**: Well-documented, object-oriented implementation
- **Prediction Examples**: Ready-to-use examples for making predictions

## 🚀 Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Required Dependencies

Install the required packages using pip:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Alternative Installation

You can also install all dependencies at once:

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following content:

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
```

## 💻 Usage

### Basic Usage

Run the complete machine learning pipeline:

```bash
python ml-classifier.py
```

This will:
1. Load and explore the Iris dataset
2. Train multiple machine learning models
3. Evaluate and compare model performance
4. Display results and make sample predictions

### Advanced Usage

You can also use the `IrisClassifier` class in your own code:

```python
from ml_classifier import IrisClassifier

# Create classifier instance
classifier = IrisClassifier()

# Run complete analysis
classifier.run_complete_analysis()

# Or run individual steps
classifier.load_data()
classifier.explore_data()
classifier.prepare_data()
classifier.train_models()
classifier.evaluate_models()
```

### Making Custom Predictions

```python
import numpy as np
from ml_classifier import IrisClassifier

# Create and train classifier
classifier = IrisClassifier()
classifier.load_data()
classifier.prepare_data()
classifier.train_models()

# Create sample data (sepal_length, sepal_width, petal_length, petal_width)
sample_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Should be Setosa

# Scale the data
sample_data_scaled = classifier.scaler.transform(sample_data)

# Get best model
best_model_name = max(classifier.results, key=lambda k: classifier.results[k]['accuracy'])
best_model = classifier.results[best_model_name]['model']

# Make prediction
prediction = best_model.predict(sample_data_scaled)
confidence = best_model.predict_proba(sample_data_scaled)

print(f"Prediction: {classifier.target_names[prediction[0]]}")
print(f"Confidence: {max(confidence[0]):.3f}")
```

## 📊 Examples

### Sample Output

```
============================================================
IRIS DATASET MACHINE LEARNING CLASSIFIER
============================================================

Loading Iris dataset...
Dataset loaded successfully!
Shape: (150, 4)
Features: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Classes: ['setosa' 'versicolor' 'virginica']

==================================================
EXPLORATORY DATA ANALYSIS
==================================================

Dataset Info:
Number of samples: 150
Number of features: 4
Number of classes: 3

Class Distribution:
setosa: 50 samples
versicolor: 50 samples
virginica: 50 samples

==================================================
TRAINING MACHINE LEARNING MODELS
==================================================

Training Random Forest...
✓ Random Forest trained successfully!
  Accuracy: 1.0000
  CV Score: 0.9583 (±0.0500)

Training Logistic Regression...
✓ Logistic Regression trained successfully!
  Accuracy: 1.0000
  CV Score: 0.9583 (±0.0669)

Training Support Vector Machine...
✓ Support Vector Machine trained successfully!
  Accuracy: 1.0000
  CV Score: 0.9750 (±0.0395)

🏆 Best Model: Support Vector Machine (Accuracy: 1.0000)
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| numpy | >=1.21.0 | Numerical computations |
| pandas | >=1.3.0 | Data manipulation and analysis |
| matplotlib | >=3.4.0 | Basic plotting and visualization |
| seaborn | >=0.11.0 | Statistical data visualization |
| scikit-learn | >=1.0.0 | Machine learning algorithms |

## 🎯 Key Components

### IrisClassifier Class Methods

- `load_data()`: Load the Iris dataset from scikit-learn
- `explore_data()`: Perform exploratory data analysis
- `visualize_data()`: Create data visualizations
- `prepare_data()`: Split and scale the data
- `train_models()`: Train multiple ML models
- `evaluate_models()`: Evaluate and compare models
- `plot_confusion_matrices()`: Visualize model performance
- `run_complete_analysis()`: Execute the full pipeline

## 🔧 Customization

You can easily customize the classifier:

```python
# Change test size
classifier.prepare_data(test_size=0.3)

# Add more models
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

# Modify the models_to_train dictionary in train_models() method
models_to_train = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Support Vector Machine': SVC(random_state=42, probability=True),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions

- Add more machine learning algorithms
- Implement hyperparameter tuning
- Add feature importance analysis
- Create interactive visualizations
- Add more datasets
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙏 Acknowledgments

- The Iris dataset was collected by Edgar Anderson and made famous by Ronald Fisher
- Built with [scikit-learn](https://scikit-learn.org/)
- Visualizations powered by [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/)
- Part of the [PyVault](../../README.md) project collection

---

**Happy Machine Learning! 🚀**

*If you found this project helpful, please consider giving it a ⭐!*
