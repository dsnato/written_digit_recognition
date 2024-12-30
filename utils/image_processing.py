from PIL import Image
import numpy as np

def preprocess_image(image_path):
    try:
        image = Image.open(image_path).convert('L')  # Converte para escala de cinza
        image = image.resize((28, 28))  # Redimensiona para 28x28
        image = np.array(image) / 255.0  # Normaliza para valores entre 0 e 1
        image = image.reshape(1, 28, 28)  # Ajusta para o formato do modelo
        return image
    except Exception as e:
        print(f"Erro no processamento da imagem: {e}")
        return None
