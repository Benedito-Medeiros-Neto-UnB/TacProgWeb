from django.urls import path
from . import views

urlpatterns = [
    path('', views.producao_list, name='producao_list'),
]