from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import SearchForm
from .models import FormNews

# Create your views here.

def news(request):
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        if form.is_valid:
            news = form.save(commit=False)
            news.save()
            return redirect('success', id=news.pk)
    else:
        form = SearchForm()
        dict = {'form': form}
    return render(request, 'form.html', context=dict)

def success(request, id):
    news = FormNews.objects.get(id=id)      
    value = round(news.predicao *100, 2)
    return render(request, 'success.html', {"news": news, "value": value})