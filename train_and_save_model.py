import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# 1. Carregar o Dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2. Criar o Modelo
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Camada de entrada
    Dense(128, activation='relu'),  # Camada oculta com 128 neurônios
    Dense(64, activation='relu'),   # Camada oculta com 64 neurônios
    Dense(10, activation='softmax') # Camada de saída (10 classes)
])

# 3. Compilar o Modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Treinar o Modelo
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# 5. Avaliar o Modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# 6. Salvar o Modelo
model.save('model/mnist_model.h5')
print("Modelo salvo em 'model/mnist_model.h5'")
