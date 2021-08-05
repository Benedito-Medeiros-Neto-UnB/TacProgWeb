"""educacao_3_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_est.views import index, elements, generic, aula, web, edu, labs, lab01, lab02, lab03, lab04, lab05, lab06, lab07, lab08, book_list, upload


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('elements/', elements),
    path('generic/', generic),
    path('aula/', aula),
    path('web/', web),
    path('edu/', edu),
    path('labs/', labs),
    path('lab01/', lab01),
    path('lab02/', lab02),
    path('lab03/', lab03),
    path('lab04/', lab04),
    path('lab05/', lab05),
    path('lab06/', lab06),
    path('lab07/', lab07),
    path('lab08/', lab08),
    path('book_list/', book_list),
    path('book_list/upload/', upload)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
