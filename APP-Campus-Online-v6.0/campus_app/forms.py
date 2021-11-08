from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Noticia, Video, WhatsAppAccount, Imagem, TextoMateria
from django.contrib.auth.models import User


class NoticiaForm(forms.ModelForm):

    usuarios = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=User.objects.exclude(is_active='False').order_by('first_name'),
            required=True)

    class Meta:
        
        model = Noticia
        fields = ['usuarios', 'titulo', 'texto', 'prioridade',
                  'link_externo', 'link_video', 'link_foto', 'autoria_midia']

class ImagemForm(forms.ModelForm):
    noticia = forms.ModelChoiceField(queryset=Noticia.objects.all())
    class Meta:
        model = Imagem
        fields = '__all__'
        

class VideoForm(forms.ModelForm):
    noticia = forms.ModelChoiceField(queryset=Noticia.objects.all())
    class Meta:
        model = Video
        fields = '__all__'

class TextoMateriaForm(forms.ModelForm):
    noticia = forms.ModelChoiceField(queryset=Noticia.objects.all())
    class Meta:
        model = TextoMateria
        fields = '__all__'


class WhatsAppAccountCreateForm(forms.ModelForm):

    class Meta:

        model = WhatsAppAccount
        fields = ['numero_telefone']
        labels = {'numero_telefone':'Número de WhatsApp do Campus'}

    def __init__(self, *args, **kwargs):

        super(WhatsAppAccountCreateForm, self).__init__(*args, **kwargs)
        self.fields['numero_telefone'].widget.attrs.update({'class' : 'numero_telefone', 'placeholder' : 'Ex.: 5561987654321'})

