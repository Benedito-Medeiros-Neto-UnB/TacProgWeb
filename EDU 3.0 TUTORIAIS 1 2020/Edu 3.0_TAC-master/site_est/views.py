from django.shortcuts import render, redirect
from django.http import FileResponse, Http404

from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import BookForm
from .models import Book
# Create your views here.


def index(request):
    
    return render(request, 'site_est/index.html')

def elements(request):
    
    return render(request, 'site_est/elements.html')

def generic(request):
    
    return render(request, 'site_est/generic.html')

def aula(request):
        
    return render(request, 'site_est/aula.html')

def web(request):
        
    return render(request, 'site_est/web.html')

def edu(request):
        
    return render(request, 'site_est/edu.html')

def labs(request):
    books = Book.objects.all()
    return render(request, 'site_est/labs.html', {'books' : books })

def lab01(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_yamin_fernanda.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab02(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_marina.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab03(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_diegod.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab04(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_patrick.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab05(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_joao.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab06(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_meu.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab07(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_cristiane.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab08(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_carolzinha.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def book_list(request):
    books = Book.objects.all()
    return render(request, 'site_est/book_list.html', {'books' : books } )

def upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/book_list')
    else:
        form = BookForm()

    return render(request, 'site_est/upload.html', {'form': form} )


