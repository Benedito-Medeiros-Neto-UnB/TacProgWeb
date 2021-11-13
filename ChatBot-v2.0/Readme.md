# Campusito ChatBot
Um projeto de um ChatBot feito em [Rasa](https://rasa.com/) para auxiliar os usuários do APP CAMPUS MULTIPLATAFORMA da Faculdade de Comunicação (FAC) da Universidade de Brasília (UnB).

# Instalação

### Linux e MacOS

Instalar um ambiente virtual python:

```
python3.8 -m venv venv
```

Atualizar o pip:

```
python -m pip install --upgrade pip
```

Instalando as dependências:

```
pip install -r requeriments.txt
```

# Treinamento

Para treinar o chatbot, só entrar na pasta do campusito e digitar:

```
rasa train
```

# Execução
Para executar o chatbot só utilizar os comandos:

```
rasa run actions
```
Esse comando irá iniciar o servidor de actions para as ações customizadas.

```
rasa shell
```

É possível interagir com o chatbot dentro do próprio terminal usando esse comando.

