from django.shortcuts import render
from sitecampus.models import Autor, Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context=context )
