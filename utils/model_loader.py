from tensorflow.keras.models import load_model
import os

def load_trained_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'model', 'mnist_model.h5')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo não encontrado no caminho: {model_path}")

    print(f"Carregando modelo do caminho: {model_path}")
    return load_model(model_path)

