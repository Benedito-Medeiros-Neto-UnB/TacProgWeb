# Campusito ChatBot

Um projeto de um ChatBot feito em [Rasa](https://rasa.com/) para auxiliar os usuários do CAMPUS ONLINE da Faculdade de Comunicação (FAC) da Universidade de Brasília (UnB).

## Configurando o projeto

Clone este repositório e, em seguida, entre no seu diretório e crie um ambiente virtual por meio do comando:

### Windows

```
python -m venv venv
```

### LINUX e MACOS

```
python3 -m venv venv
```

Agora, para ativar o ambiente:

### Windows

```
venv/Scripts/activate
```

### LINUX e MACOS

```
source venv/bin/activate
```

Feito isso, basta instalar as dependências que estamos utilizando. Primeiramente, vamos verificar o [pip](https://pypi.org/project/pip/):

```
python -m pip install --upgrade pip
```

Agora, instalando as dependências:

```
pip install -r requirements.txt
```

## Treinando a aplicação

Entre no diretório 'bot' com o seu ambiente virtual ativo. Feito isso, observe que existe um Makefile. Para treinar o bot, digite o seguite comando:

### LINUX e MACOS

```
sudo make train
```

Uma vez treinado, deve-se subir o servidor de actions com o seguinte comando:

```
rasa run actions
```
É importante frisar que se os dois passos anteriores não forem feitos, o bot não irá funcionar da forma esperada!

## Rodando a aplicação Web

Caso não ocorra nenhum erro treinando o bot, basta ativar o webchat agora. Para isso, abra outra janela no seu terminal e digite:

### LINUX e MACOS

```
sudo make webchat
```

Com esse comando rodando, basta entrar na pasta **modules/webchat** do diretório raiz e abrir o arquivo _index.html_.

Observe que no canto direito inferior aparece um ícone com o ChatBot ativado. Ainda, vale ressaltar que essa página é local.

## Rodando a aplicação Telegram

Caso não ocorra nenhum erro treinando o bot, basta ativar o telegram agora. Para isso:

### LINUX e MACOS

Primeiramente, deve-se subir o servidor utilizando o [ngrok](https://ngrok.com/). Em um terminal, digite:

```
ngrok http 5001
```

Feito isso, copie o segundo _Forwarding_ link HTTPS e copie ele em _webhook_url_ dentro do arquivo _credentials_ que se encontra dentro da pasta _bot_. _CUIDADO_: o atributo _webhook_url_ deve estar no seguinte formato: < LINK HTTPS >/webhooks/telegram/webhook

Uma vez atribuido o link do servidor e este encontra-se ativo, basta rodar em um terminal diferente:

```
sudo make telegram
```

Agora, abra o telegram e encontre o bot por meio do nickname de @campusito_bot. Pronto!
