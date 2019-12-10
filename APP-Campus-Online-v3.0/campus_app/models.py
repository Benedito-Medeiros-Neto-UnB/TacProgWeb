from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    cod_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_noticia")
    titulo = models.CharField(max_length=200)
    palavras_chave = models.CharField(max_length=200, null=True, blank=True, default='')
    resumo = models.CharField(max_length=300, null=True, blank=True, default='')
    texto = models.TextField(max_length=600)
    prioridade = models.IntegerField(default=0)
    link_externo = models.CharField(max_length=300, null=True, blank=True, default='')
    link_foto = models.CharField(max_length=300, null=True, blank=True, default='')
    link_audio = models.CharField(max_length=300, null=True, blank=True, default='')
    link_video = models.CharField(max_length=300, null=True, blank=True, default='')
    link_georreferenciamento = models.CharField(max_length=300, null=True, blank=True, default='')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    dia_publicacao = models.DateField(auto_now_add=True)
