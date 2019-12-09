from django import forms

from .models import FormNews

class SearchForm(forms.ModelForm):
    class Meta:
        model = FormNews
        fields = ( 'titulo', 'url','texto')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })