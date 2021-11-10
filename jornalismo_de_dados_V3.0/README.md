# Projeto Realizado durante o Semestre 2021/1 UNB

- Instalação do projeto pode ser feita seguindo os passos a seguir:
1) Verificar se possui o python instalado.
2) Após verificar se possuir o python instalado, vamos para a pasta do projeto e executamos o comando:
- python manage.py runserver
3) Pronto projeto estará rodando no localhost:8000.

Instalar em servidor de produção (comandos de Ubuntu):
```
sudo apt-get update

sudo apt-get install python3  python3-pip

git clone https://github.com/Benedito-Medeiros-Neto-UnB/WikiJour-Data.git

cd WikiJour-Data

pip3 install -r requirements.txt

python3 manage.py collectstatic
```

Para executar na porta 8000 sem o Apache:
```
python3 ./manage.py runserver 0.0.0.0:8000
```

Para executar na porta 80 com o Apache:

Criar o myproject/wsgi_production.py e colocar as configurações desejadas (DJANGO_DEBUG, DJANGO_DATABASE_NAME, etc) e alterar no myproject/settings.py igual foi feito com o DJANGO_DEBUG.
```
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
os.environ.setdefault('DJANGO_DEBUG', 'True')
os.environ.setdefault('DJANGO_DATABASE_NAME', '/home/django_websites/WikiJour-Data/myproject/project.db')
application = get_wsgi_application()
```

Configurar o Apache para iniciar pelo wsgi_production.py ao invés do wsgi.py
```
<VirtualHost *:80>
    ServerName wikijour.filosofiacienciaarte.org
    ServerAlias wikijour.filosofiacienciaarte.org *.wikijour.filosofiacienciaarte.org
    DocumentRoot /home/django_websites/WikiJour-Data/myproject

    #Alias /static /home/django_websites/WikiJour-Data/myproject/static
    <Directory /home/django_websites/WikiJour-Data/myproject/static>
        Require all granted
    </Directory>

    <Directory /home/django_websites/WikiJour-Data/myproject>
        <Files wsgi_production.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess wikijour.filosofiacienciaarte.org python-path=/home/django_websites/WikiJour-Data python-home=/home/django_websites/django-virtualenv
    WSGIProcessGroup wikijour.filosofiacienciaarte.org
    WSGIScriptAlias / /home/django_websites/WikiJour-Data/myproject/wsgi_production.py

</VirtualHost>
```
Reiniciar o apache sempre que uma alteração for feita no código:
```
$ sudo systemctl reload apache2
```

Acesso ao site:

http://wikijour.filosofiacienciaarte.org/
