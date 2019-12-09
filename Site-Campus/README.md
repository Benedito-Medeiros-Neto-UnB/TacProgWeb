# README
## *algums comandos para ajudar a iniciar o trabalho*

### configuracao exclusiva para **linux**
#### para informacao mais detalhada e outras plataformas
[Clique_aqui](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

### primeiro check a versao do python instalada pois precisamos
### do python > 3.6.6
- python3 -V

### Caso esteja tudo certo temos que instalar o pip ( um Python Package Index tool)
- sudo apt install python3-pip

### agora precisamos preparar um ambiente virtual para trabalho
- sudo pip3 install virtualenvwrapper

#### adicione a segintes linhas ao seu .bashrc para configurar o path
```
 export WORKON_HOME=$HOME/.virtualenvs
 export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
 export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
 export PROJECT_HOME=$HOME/Devel
 source /usr/local/bin/virtualenvwrapper.sh
 ```

#### para aplicar as modificações precisamos recarregar o arquivo
> source ~/.bashrc

### comando para configurar o ambiente virtual
##### serve pra criar um novo ambiente
- mkvirtualenv **nome_do_ambiente_vitual**
##### serve para sair do ambiente (só pode ser usado dentro de um ambiente)
- deactivate 
##### lista os ambiente existentes
- workon 
##### inicia um ambiente para trabalho
- workon **nome_do_ambiente_vitual**
##### exclui o ambiente
- rmvirtualenv name_of_environment 

### Agora sim vamos instalar o django (lembre-se de inciar o ambiente virtual antes)
#### vamos instalar o django no ambiente virtual
- pip3 install django
##### para testar se o django foi instalado corretamente 
- python3 -m django --version

### Bibliotecas usadas
#### Usado no select do admin
- pip install django-model-choices
#### Usado na models
- pip install Pillow
#### Usado para criar tags nos posts
- pip install django-taggit 
#### Usado no content da model
- pip install django-richtextfield

### Agora vamos testar a instalação do django
#### dentro da pasta do projeto (a pasta com manage.py e duas pastas) rode
- python3 manage.py runserver 
##### se funcionar irá aparecer mais ou menos isso
```
Django version 2.2.7, using settings 'campusonline.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## agora é só diversão 😜 
