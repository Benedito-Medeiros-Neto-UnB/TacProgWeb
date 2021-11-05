from django.db import models
from django.contrib.auth.models import User


def get_full_name(self):

    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_full_name)


class Noticia(models.Model):

    usuarios = models.ManyToManyField(User, related_name="usuario_noticia")
    titulo = models.CharField(max_length=200)
    palavras_chave = models.CharField(max_length=200, null=True, blank=True, default='')
    resumo = models.CharField(max_length=500, null=True, blank=True, default='')
    texto = models.TextField(max_length=600)
    prioridade = models.IntegerField(default=0)
    link_externo = models.CharField(max_length=300, null=True, blank=True, default='')
    link_foto = models.CharField(max_length=300, null=True, blank=True, default='')
    link_audio = models.CharField(max_length=300, null=True, blank=True, default='')
    link_video = models.CharField(max_length=300, null=True, blank=True, default='')
    autoria_midia = models.CharField(max_length=300, null=True, blank=True, default='')
    link_georreferenciamento = models.CharField(max_length=300, null=True, blank=True, default='')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    dia_publicacao = models.DateField(auto_now_add=True)

class Imagem(models.Model):
    link_foto_long_form =models.CharField(max_length=300, null=True, blank=True, default='')
    autoria_midia_imagem = models.CharField(max_length=300, null=True, blank=True, default='')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

#criando nova tabela para armazenar vários vídeos referentes a uma mesma notícia
class Video(models.Model):
    link_video_long_form = models.CharField(max_length=300, null=True, blank=True, default='')
    autoria_midia_video = models.CharField(max_length=300, null=True, blank=True, default='')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

class TextoMateria(models.Model):
    subtitulo = models.CharField(max_length=200, null=True, blank=True, default='')
    texto_materia = models.TextField(max_length=2000)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)


class WhatsAppAccount(models.Model):

    cod = models.AutoField(primary_key=True, null=False)
    numero_telefone = models.CharField(max_length=20, null=False)

    def __str__(self):

        return self.numero_telefone

