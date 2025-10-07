# Agro-Inteligência

- **FNN (Feedforward Neural Network)**: para dados tabulares, como informações de solo e clima.  
- **CNN (Convolutional Neural Network)**: para classificação de imagens de folhas, identificando se estão saudáveis ou doentes.  
- **RNN (LSTM)**: para analisar notas de campo e classificá-las como urgentes ou de rotina.

O objetivo do projeto é criar um protótipo funcional que permita coletar dados reais e gerar insights inteligentes com eles, mesmo com datasets pequenos.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **cnn_service/**: contém o modelo CNN, scripts de pré-processamento de imagens e API Flask para ingestão e inferência.  
- **fnn_service/**: contém o modelo FNN, script de treinamento e API Flask para ingestão e inferência de dados tabulares.  
- **rnn_service/**: contém o modelo LSTM, script de treinamento e API Flask para ingestão e inferência de notas de texto.  
- **uploads/**: pasta para armazenar imagens enviadas para treinamento da CNN, separadas em `saudavel` e `doente`.  
- **.venv/**: ambiente virtual Python.  
- **prepare_cnn_data.py** e outros scripts auxiliares.  
- **README.md**: este arquivo, com todas as instruções.

## Como Rodar o Projeto

1. **Preparação do ambiente**:  
   Certifique-se de ter o Python 3.10 ou superior. Crie um ambiente virtual e instale as dependências:

   - No Windows:  
     `python -m venv .venv`  
     `.venv\Scripts\activate`  
   - No Linux/Mac:  
     `python -m venv .venv`  
     `source .venv/bin/activate`  

   Depois, instale as bibliotecas necessárias:  
   `pip install tensorflow numpy pillow flask requests`

2. **Executando as APIs de ingestão**:  
   Cada serviço possui um endpoint `/log` que recebe dados via POST:

   - **CNN**: envia imagens em Base64 com o rótulo (`saudavel` ou `doente`).  
   - **FNN**: envia dados de solo e clima em formato JSON.  
   - **RNN**: envia notas de texto com rótulos (`urgente` ou `rotina`).  

   Basta rodar o script `app.py` de cada serviço para iniciar a API.

3. **Criando o dataset próprio**:  
   Use as APIs para enviar dados reais ou simulados. Para cada tipo de dado, o projeto recomenda:

   - **CNN**: pelo menos 20 imagens por classe (saudável/doente).  
   - **FNN**: pelo menos 30 registros tabulares de solo e clima, com uma coluna alvo binária (ex: rendimento alto = 1 ou 0).  
   - **RNN**: pelo menos 40 notas de texto, 20 urgentes e 20 de rotina.

4. **Treinamento dos modelos**:  
   Cada serviço possui um script de treinamento (`train_cnn.py`, `train_fnn.py`, `train_rnn.py`) que lê os dados coletados, constrói e treina o modelo correspondente.  
   Os modelos treinados serão salvos para uso posterior na inferência.

5. **Inferência em tempo real**:  
   Cada serviço possui um endpoint `/predict`. Você pode enviar um único dado (imagem, registro de solo ou nota de texto) e receber a previsão do modelo treinado.  
   Por exemplo, para a CNN, você pode rodar `processar_img.py` enviando a imagem decodificada, e ele retornará a classe prevista e a probabilidade.

Quer que eu faça essa versão visual?
```
