from django.db import models
import datetime
import django


def accept():
    return(
        (True, 'Sim'),
        (False, 'Nao'),
    )

# Create your models here.
class Linguagem(models.Model):
    lingua = models.CharField('Lingua',max_length=30, default="Português",unique=True)
    
    def __str__(self):
        return self.lingua

class Jornal(models.Model):
    nome = models.CharField('Nome do Jornal', max_length=50,unique=True)
    email= models.CharField('e-Mail do Jornal', max_length=100)
    site=models.CharField('site do Jornal', max_length=100)

    def __str__(self):
        return self.jornal

class Categoria(models.Model):
    categoria= models.CharField("Categoria",max_length=50,unique=True)

    def __str__(self):
        return self.categoria


class Tema(models.Model):
    tema=models.CharField("Tema",max_length=60,unique=True)
    def __str__(self):
        return self.tema

class Envolvidos(models.Model):
    nome=models.CharField("Nome",max_length=200,unique=True)
    def __str__(self):
        return self.nome

class Tipo_midia(models.Model):
    tipo = models.CharField('Tipo de Mídia',max_length=254,help_text="Nome da produção", unique=True)

class Formato(models.Model):
    formato=models.CharField("Formato",max_length=6,unique=True)
    midia = models.ForeignKey(Tipo_midia, on_delete=models.PROTECT)

class Producao(models.Model):
    titulo=models.CharField('Título',max_length=254,help_text="Nome da produção",unique=True)
    descricao=models.TextField('Descrição', blank=True)
    data = models.DateField('Data do Documento', default=django.utils.timezone.now, help_text="Use formato dd/mm/AAAA")
    accepted = models.BooleanField('Accept file', choices=accept(), default=False)
    file = models.FileField(upload_to='producoes/', blank=True) #, validators=[validate_producao]
    url = models.URLField('URL para Documento', blank=True)
    formato = models.ForeignKey(Formato, on_delete=models.PROTECT)
    jornal = models.ForeignKey(Jornal, on_delete=models.PROTECT,blank=True)
    linguagem = models.ForeignKey(Linguagem,on_delete= models.PROTECT)
    categoria = models.ForeignKey(Categoria,on_delete= models.SET('Não categorizado'))
   
    def aprove(self):
        self.accepted=True
   
    def __str__(self):
        return self.titulo



class Tema_producao(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    producao = models.ForeignKey(Producao, on_delete=models.PROTECT)

class Envolvidos_producao(models.Model):
    role = models.CharField('Roles',max_length=300,help_text="Papeis no desenvolvimento da produção")
    producao = models.ForeignKey(Producao, on_delete=models.PROTECT)
    envolvido = models.ForeignKey(Envolvidos, on_delete=models.PROTECT)