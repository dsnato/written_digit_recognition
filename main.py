from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Carregar o modelo treinado
model = load_model('mnist_model.h5')

# Widget para desenhar
class DrawWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 1)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.graphics import Line, Color
    from utils.model_loader import load_model
    from utils.image_processing import preprocess_image
    import os

    class DrawingWidget(BoxLayout):
        def on_touch_down(self, touch):
            with self.canvas:
                Color(0, 0, 0)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)

        def on_touch_move(self, touch):
            touch.ud['line'].points += [touch.x, touch.y]

        def save_image(self):
            image_path = 'assets/test_images/drawing.png'
            self.export_to_png(image_path)
            return image_path

    class MNISTApp(App):
        def build(self):
            self.model = load_model()
            self.widget = DrawingWidget()
            return self.widget

        def classify_image(self):
            image_path = self.widget.save_image()
            image = preprocess_image(image_path)
            if image is not None and self.model:
                prediction = self.model.predict(image)
                digit = prediction.argmax()
                self.root.ids.result_label.text = f'Resultado: {digit}'
            else:
                self.root.ids.result_label.text = 'Erro na classificação!'

    if __name__ == '__main__':
        os.makedirs('assets/test_images', exist_ok=True)
        MNISTApp().run()
