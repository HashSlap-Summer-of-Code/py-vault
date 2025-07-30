from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense

(X_train, Y_train),(X_test, Y_test) = mnist.load_data()
X_train = X_train / 255.0
X_test = X_test / 255.0

model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(128, activation='relu'),
    Dense(256, activation='relu'),
    Dense(10, activation='softmax'),
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=10, batch_size=32)

loss,accuracy = model.evaluate(X_test,Y_test)
print(f"Model Accuracy: {accuracy:.4f}")

model.save("mnist_model.keras")