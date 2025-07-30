# MNIST Basic Neural Network (TensorFlow)

This project demonstrates a simple neural network for handwritten digit classification using the MNIST dataset.

## Files Included

- `mnist-basic-nn.py` - Script to train a basic neural network model on the MNIST dataset using TensorFlow.
- `predict.py` - Script to load the trained model and predict digits from custom image input.
- `mnist_model.keras` - Saved trained model (output of training).
- `my_digit.png` - Sample digit image used for prediction (you can replace this with your own).

---

## Model Details

- Framework: TensorFlow (Keras)
- Layers:
  - Input layer: Flatten
  - Hidden layers: Dense (ReLU)
  - Output layer: Dense (Softmax)
- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy

---

## Installation

Install the required packages:

```bash
    pip install tensorflow matplotlib pillow
