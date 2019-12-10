from django.contrib import admin
from .models import Producao, Tema, Categoria, Jornal, Linguagem, Tipo_midia, Formato

admin.site.register(Producao)
admin.site.register(Tema)
admin.site.register(Categoria)
admin.site.register(Jornal)
admin.site.register(Linguagem)
admin.site.register(Tipo_midia)
admin.site.register(Formato)

# Register your models here.
