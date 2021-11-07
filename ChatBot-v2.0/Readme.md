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

# Features adicionais

Instalando o componente rasa x:

```
pip3 install rasa x
```

A ferramenta rasa x permite uma iteração mais visual com o chatbot.

#Treinamento
Para treinar o chatbot, só entrar na pasta do campusito e digitar:

```
rasa train
```

# Execução
Para executar o chatbot só utilizar os comandos:

```
rasa shell
```

É possível interagir com o chatbot dentro do próprio terminal.

```
rasa x
```

O rasa x, quando ativo, abre automaticamente uma página que abre uma janela hospedada no localhost, sendo possível a iteração gráfica com o chatbot.
