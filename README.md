# written_digit_recognition
Título do Projeto: Reconhecimento de Dígitos Escritos à Mão usando Inteligência Artificial e uma Interface Gráfica com Kivy.

Objetivo:

Criar um aplicativo simples em Python e Kivy que:
	1.	Utiliza Machine Learning (Deep Learning) para reconhecer dígitos manuscritos.
	2.	Integra uma interface gráfica em Kivy para o usuário desenhar um dígito (0-9) e visualizar o resultado.

Tecnologias e Bibliotecas:
	1.	Python (linguagem principal).
	2.	Kivy (para a interface gráfica).
	3.	TensorFlow/Keras (para o modelo de Machine Learning pré-treinado).
	4.	NumPy e Pillow (para manipulação da imagem desenhada).
	5.	MNIST Dataset (banco de dados de dígitos manuscritos).

Funcionamento:
	1.	A interface Kivy terá uma área para desenhar o dígito e um botão “Classificar”.
	2.	Quando o usuário desenhar o dígito e clicar em “Classificar”:
	•	A imagem desenhada será capturada e processada.
	•	Um modelo de Deep Learning previamente treinado (baseado no dataset MNIST) irá prever o dígito.
	•	O resultado (por exemplo, “Dígito Reconhecido: 3”) será exibido na tela.
	3.	O modelo de Deep Learning será carregado de forma simples e estará pronto para uso.

Etapas de Implementação:
	1.	Preparação do modelo de Machine Learning:
	•	Treinar ou carregar um modelo simples de classificação de imagens baseado no MNIST.
	•	Utilizar TensorFlow/Keras para criar e salvar o modelo em um arquivo .h5 (modelo treinado).
	2.	Criação da interface gráfica com Kivy:
	•	Desenvolver uma interface básica com uma área para desenhar (Canvas do Kivy).
	•	Adicionar um botão para classificar a imagem.
	•	Mostrar o resultado na tela.
	3.	Processamento da imagem:
	•	Converter o desenho feito no Kivy em uma imagem de 28x28 pixels (formato exigido pelo modelo MNIST).
	•	Transformar a imagem em um array NumPy para alimentar o modelo de Machine Learning.
	4.	Integração do modelo e interface:
	•	Carregar o modelo pré-treinado no Kivy e use-o para fazer previsões.

Resultado Esperado:
	•	Uma janela será aberta com uma área para desenhar.
	•	Ao desenhar um número de 0 a 9 e clicar no botão “Classificar”, o sistema mostrará o dígito reconhecido.

Entrega Final:

O projeto será apresentado com:
	1.	O código-fonte do aplicativo.
	2.	Prints da interface funcionando.
	3.	Explicação do modelo e do funcionamento geral.
