from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['cod_usuario', 'titulo', 'texto', 'prioridade',
                  'link_externo', 'link_video', 'link_foto']
