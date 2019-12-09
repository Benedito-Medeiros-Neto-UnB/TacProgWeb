from django.urls import path
from sitecampus import views


urlpatterns = [
    path('', views.index, name='index'),
]