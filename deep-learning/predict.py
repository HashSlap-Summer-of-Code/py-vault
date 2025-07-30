import numpy as np
import tensorflow as tf
from PIL import Image

# Load image
def load_and_prepare_image(path):
    image = Image.open(path).convert('L')
    image = image.resize((28, 28))
    image = np.array(image)

    image = 255 - image     # For Light Background

    image = image / 255.0
    image = image.reshape(1, 28, 28)
    return image

# Load model
model = tf.keras.models.load_model('mnist_model.keras')

# Load your image
image_path = 'img.png'
image = load_and_prepare_image(image_path)

# Predict
prediction = model.predict(image)
predicted_digit = np.argmax(prediction)

print(f"Predicted digit: {predicted_digit}")
