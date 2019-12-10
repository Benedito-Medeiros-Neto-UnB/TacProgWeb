# APP-Campus-Online-v3.0
Repositório para o desenvolvimento da nova versão do APP Campus Online.

## Environment
Virtualenv é um ambiente virtual dp python que permite instalar bibliotecas para cada aplicação isoladas da máquina.

Em relação ao git, o env fica no .gitignore

Depois de clonado o repositório, é necessário criar um env (virtualenv), ativá-lo e instalar o que for necessário, seguem os comandos:

1. virtualenv -p python3 env (comando para criar um virtualenv)
2. source env/bin/activate (comando para ativar o env)
* Sempre que for instalar algo ou executar a aplicação é necessário usar esse comando para ativar o ambiente
* Se quiser sair do ambiente basta digitar: deactivate
3. pip install -r requirements.txt (comando para instalar os requisitos do env do projeto, django por exemplo)
* É possível utilizar esse 3º comando visto que o comando pip freeze mostra tudo que está instalado no env, e o seguinte comando:
* pip freeze > requirements.txt 
* grava nesse arquivo txt o que está instalado. 



