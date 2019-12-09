from django.db import models
from modelchoices import Choices
from taggit.managers import TaggableManager


# model de Post
class Post(models.Model):

    EstadoPub = (
        ('1' , 'Rascunho'),
        ('2' , 'Em Revisão'),
        ('3' , 'Pronto'),
    )

    HIERARQUIA = (
        ('1' , 'Primaria'),
        ('2' , 'Secundaria'),
        ('3' , 'Terciaria'),
    )

    titulo = models.CharField(max_length=100)

    sutia = models.TextField(max_length=200, blank=True, null=True)

    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)

    editoria = models.ForeignKey('Editoria', on_delete=models.SET_NULL, null=True)

    conteudo = models.TextField( default="")

    tags = TaggableManager()

    estado = models.CharField(max_length=1, choices=EstadoPub, blank=False, default="1", null=False)

    semestre_publicação = models.CharField(max_length=6, blank=False, null=False, help_text=u"20xx/x")

    hierarquia = models.CharField(max_length=1, choices=HIERARQUIA, blank=False, default="", null=False)

    post_image = models.CharField( max_length=90, blank=True, null=True, help_text="url da imagem hospedada")

    def __str__ (self):
        return self.titulo

    def get_asolute_url(self):
        return reverse ('detalhe_post', args=[str(self.id)])


# model de Editorias
class Editoria(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.TextField(max_length=500)

    def __str__ (self):
        return self.nome

    def get_asolute_url(self):
        return reverse ('detalhe_editoria', args=[str(self.id)])


# model de Autor   

class Autor(models.Model):


    autor_avatar = models.ImageField(upload_to='assets/images', blank=True, null=True)

    primeiro_nome = models.CharField(max_length=100)

    sobrenome = models.CharField(max_length=100)

    nome_completo = models.CharField(max_length=100)

    semestre = models.CharField(max_length=6, blank=False, null=False, help_text=u"20xx/x")

    class Meta:
        ordering = ['primeiro_nome', 'sobrenome']

    def get_absolute_url(self):
        return reverse('detalhe_autor', args=[str(self.id)])

    def __str__(self):
        return f'{self.primeiro_nome} {self.sobrenome}'
