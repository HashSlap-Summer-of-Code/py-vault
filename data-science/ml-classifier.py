#!/usr/bin/env python3
"""
Machine Learning Classifier using Scikit-Learn

This script demonstrates a basic machine learning classifier using the famous Iris dataset.
It includes data loading, preprocessing, model training, evaluation, and visualization.

Author: PyVault Contributors
Date: August 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
    confusion_matrix
)
import warnings
warnings.filterwarnings('ignore')


class IrisClassifier:
    """
    A comprehensive machine learning classifier for the Iris dataset.
    
    This class provides methods for data loading, preprocessing, training
    multiple models, evaluation, and visualization.
    """
    
    def __init__(self):
        """Initialize the IrisClassifier with default parameters."""
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = StandardScaler()
        self.models = {}
        self.results = {}
        
    def load_data(self):
        """
        Load the Iris dataset from scikit-learn.
        
        Returns:
            tuple: Feature matrix X and target vector y
        """
        print("Loading Iris dataset...")
        iris = load_iris()
        self.X = iris.data
        self.y = iris.target
        self.feature_names = iris.feature_names
        self.target_names = iris.target_names
        
        # Convert to DataFrame for better visualization
        self.df = pd.DataFrame(self.X, columns=self.feature_names)
        self.df['target'] = self.y
        self.df['target_name'] = [self.target_names[i] for i in self.y]
        
        print(f"Dataset loaded successfully!")
        print(f"Shape: {self.X.shape}")
        print(f"Features: {self.feature_names}")
        print(f"Classes: {self.target_names}")
        
        return self.X, self.y
    
    def explore_data(self):
        """Perform exploratory data analysis on the dataset."""
        print("\n" + "="*50)
        print("EXPLORATORY DATA ANALYSIS")
        print("="*50)
        
        # Basic statistics
        print("\nDataset Info:")
        print(f"Number of samples: {len(self.df)}")
        print(f"Number of features: {len(self.feature_names)}")
        print(f"Number of classes: {len(self.target_names)}")
        
        # Class distribution
        print("\nClass Distribution:")
        class_counts = self.df['target_name'].value_counts()
        for class_name, count in class_counts.items():
            print(f"{class_name}: {count} samples")
        
        # Statistical summary
        print("\nStatistical Summary:")
        print(self.df[self.feature_names].describe())
    
    def visualize_data(self):
        """Create visualizations to understand the data better."""
        print("\nCreating data visualizations...")
        
        # Set up the plotting style
        plt.style.use('default')
        sns.set_palette("husl")
        
        # 1. Pairplot showing relationships between features
        plt.figure(figsize=(12, 10))
        sns.pairplot(self.df, hue='target_name', diag_kind='hist')
        plt.suptitle('Pairplot of Iris Features', y=1.02)
        plt.tight_layout()
        plt.show()
        
        # 2. Correlation heatmap
        plt.figure(figsize=(8, 6))
        correlation_matrix = self.df[self.feature_names].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Feature Correlation Heatmap')
        plt.tight_layout()
        plt.show()
    
    def prepare_data(self, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets and scale the features.
        
        Args:
            test_size (float): Proportion of data for testing (default: 0.2)
            random_state (int): Random state for reproducibility (default: 42)
        """
        print(f"\nSplitting data into training ({1-test_size:.0%}) and testing ({test_size:.0%}) sets...")
        
        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, stratify=self.y
        )
        
        # Scale the features
        print("Scaling features using StandardScaler...")
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"Training set shape: {self.X_train.shape}")
        print(f"Testing set shape: {self.X_test.shape}")
    
    def train_models(self):
        """Train multiple machine learning models and compare their performance."""
        print("\n" + "="*50)
        print("TRAINING MACHINE LEARNING MODELS")
        print("="*50)
        
        # Define models to train
        models_to_train = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
            'Support Vector Machine': SVC(random_state=42, probability=True)
        }
        
        # Train each model
        for name, model in models_to_train.items():
            print(f"\nTraining {name}...")
            
            # Use scaled data for training
            model.fit(self.X_train_scaled, self.y_train)
            self.models[name] = model
            
            # Make predictions
            y_pred = model.predict(self.X_test_scaled)
            
            # Calculate metrics
            accuracy = accuracy_score(self.y_test, y_pred)
            
            # Cross-validation score
            cv_scores = cross_val_score(model, self.X_train_scaled, self.y_train, cv=5)
            
            # Store results
            self.results[name] = {
                'model': model,
                'predictions': y_pred,
                'accuracy': accuracy,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std()
            }
            
            print(f"✓ {name} trained successfully!")
            print(f"  Accuracy: {accuracy:.4f}")
            print(f"  CV Score: {cv_scores.mean():.4f} (±{cv_scores.std():.4f})")
    
    def evaluate_models(self):
        """Evaluate and compare the performance of all trained models."""
        print("\n" + "="*50)
        print("MODEL EVALUATION RESULTS")
        print("="*50)
        
        # Create comparison DataFrame
        comparison_data = []
        for name, result in self.results.items():
            comparison_data.append({
                'Model': name,
                'Accuracy': result['accuracy'],
                'CV Mean': result['cv_mean'],
                'CV Std': result['cv_std']
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        comparison_df = comparison_df.round(4)
        print("\nModel Comparison:")
        print(comparison_df.to_string(index=False))
        
        # Find best model
        best_model_name = comparison_df.loc[comparison_df['Accuracy'].idxmax(), 'Model']
        best_accuracy = comparison_df.loc[comparison_df['Accuracy'].idxmax(), 'Accuracy']
        print(f"\n🏆 Best Model: {best_model_name} (Accuracy: {best_accuracy:.4f})")
        
        # Detailed evaluation for best model
        print(f"\nDetailed Classification Report for {best_model_name}:")
        best_predictions = self.results[best_model_name]['predictions']
        print(classification_report(self.y_test, best_predictions, target_names=self.target_names))
    
    def plot_confusion_matrices(self):
        """Plot confusion matrices for all trained models."""
        print("\nCreating confusion matrices...")
        
        n_models = len(self.results)
        fig, axes = plt.subplots(1, n_models, figsize=(5*n_models, 4))
        
        if n_models == 1:
            axes = [axes]
        
        for idx, (name, result) in enumerate(self.results.items()):
            cm = confusion_matrix(self.y_test, result['predictions'])
            
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=self.target_names, 
                       yticklabels=self.target_names,
                       ax=axes[idx])
            
            axes[idx].set_title(f'{name}\nAccuracy: {result["accuracy"]:.3f}')
            axes[idx].set_xlabel('Predicted')
            axes[idx].set_ylabel('Actual')
        
        plt.tight_layout()
        plt.show()
    
    def run_complete_analysis(self):
        """Run the complete machine learning pipeline."""
        print("\n" + "="*60)
        print("IRIS DATASET MACHINE LEARNING CLASSIFIER")
        print("="*60)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Explore data
        self.explore_data()
        
        # Step 3: Visualize data (optional - can be commented out for batch runs)
        # self.visualize_data()
        
        # Step 4: Prepare data
        self.prepare_data()
        
        # Step 5: Train models
        self.train_models()
        
        # Step 6: Evaluate models
        self.evaluate_models()
        
        # Step 7: Plot confusion matrices (optional)
        # self.plot_confusion_matrices()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)


def main():
    """Main function to demonstrate the Iris classifier."""
    # Create classifier instance
    classifier = IrisClassifier()
    
    # Run complete analysis
    classifier.run_complete_analysis()
    
    # Example of making predictions on new data
    print("\n" + "="*50)
    print("PREDICTION EXAMPLE")
    print("="*50)
    
    # Create sample data for prediction
    sample_data = np.array([[5.1, 3.5, 1.4, 0.2],  # Should be Setosa
                           [6.2, 2.8, 4.8, 1.8],  # Should be Virginica
                           [5.7, 2.8, 4.1, 1.3]]) # Should be Versicolor
    
    # Scale the sample data
    sample_data_scaled = classifier.scaler.transform(sample_data)
    
    # Get the best model
    best_model_name = max(classifier.results, key=lambda k: classifier.results[k]['accuracy'])
    best_model = classifier.results[best_model_name]['model']
    
    # Make predictions
    predictions = best_model.predict(sample_data_scaled)
    probabilities = best_model.predict_proba(sample_data_scaled)
    
    print(f"Using best model: {best_model_name}")
    print("\nSample predictions:")
    for i, (sample, pred, prob) in enumerate(zip(sample_data, predictions, probabilities)):
        pred_class = classifier.target_names[pred]
        max_prob = max(prob)
        print(f"Sample {i+1}: {sample} -> {pred_class} (confidence: {max_prob:.3f})")


if __name__ == "__main__":
    main()
