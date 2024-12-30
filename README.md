🚀 Reconhecimento de Dígitos Manuscritos com Kivy e TensorFlow
Este projeto utiliza Kivy para a interface gráfica e TensorFlow/Keras para reconhecimento de dígitos manuscritos usando um modelo treinado no dataset MNIST.

📚 Índice
Pré-requisitos
Estrutura do Projeto
Instalação
Treinamento do Modelo
Execução do Aplicativo
Como Usar
Possíveis Erros e Soluções

✅ 1. Pré-requisitos
Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

Python 3.8 ou superior
Pip (gerenciador de pacotes do Python)
PyCharm (opcional, mas recomendado)

📂 2. Estrutura do Projeto

bash
Copiar código
mnist_app/
├── main.py                # Arquivo principal do aplicativo Kivy
├── train_and_save_model.py # Script para treinar e salvar o modelo MNIST
├── model/
│   ├── mnist_model.h5     # Modelo treinado salvo (será gerado)
├── assets/
│   ├── test_images/       # Imagens temporárias salvas pelo app
├── ui/
│   ├── main.kv            # Interface do aplicativo
├── utils/
│   ├── image_processing.py # Pré-processamento das imagens
│   ├── model_loader.py     # Carregamento do modelo
└── README.md              # Documentação do projeto

⚙️ 3. Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/mnist_app.git
cd mnist_app

Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
cmd
Copiar código
.\venv\Scripts\activate

Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Instale as dependências necessárias:

bash
Copiar código
pip install kivy tensorflow pillow numpy

🧠 4. Treinamento do Modelo
Se você ainda não tiver o arquivo mnist_model.h5, execute o script de treinamento:

bash
Copiar código
python train_and_save_model.py
Isso vai:
Treinar um modelo simples com o dataset MNIST.
Salvar o modelo em: model/mnist_model.h5.

▶️ 5. Execução do Aplicativo
Após garantir que o modelo está disponível, execute o aplicativo com:

bash
Copiar código
python main.py
Se tudo estiver correto, uma interface gráfica abrirá para interação.

🖥️ 6. Como Usar
Abra o aplicativo.
Desenhe um número (0-9) na área branca.
Clique no botão "Classificar".
O número desenhado será reconhecido e exibido na tela com a confiança da predição.
Clique em "Limpar" para desenhar novamente.

🛡️ 7. Possíveis Erros e Soluções

❗ Erro: Arquivo mnist_model.h5 não encontrado
Causa: O modelo não foi treinado ou não está na pasta correta.
Solução: Execute:
bash
Copiar código
python train_and_save_model.py
❗ Erro: Módulo kivy ou tensorflow não encontrado
Causa: As bibliotecas não foram instaladas corretamente.
Solução: Execute:
bash
Copiar código
pip install kivy tensorflow pillow numpy
❗ Erro: Permissão negada ao acessar mnist_model.h5
Causa: Permissões incorretas no arquivo.
Solução:
Clique com o botão direito no arquivo mnist_model.h5.
Vá para Propriedades > Segurança.
Certifique-se de que seu usuário tem Leitura e Execução.

💡 8. Melhorias Futuras
Adicionar suporte para mais tipos de imagens.
Melhorar a interface gráfica.
Permitir salvar os resultados em um arquivo de texto.

🤝 9. Contribuição
Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades! Basta abrir uma Pull Request.

📄 10. Licença
Este projeto é licenciado sob a MIT License.

Feito com ❤️ por Renato Samico
Se precisar de ajuda, entre em contato! 🚀
