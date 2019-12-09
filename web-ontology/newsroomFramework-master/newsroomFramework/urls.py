"""newsroomFramework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from cms.views import *
from kms.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kms/$', kms),
    url(r'^add/$', ArticleCreateView.as_view(), name='article-add'),
    url(r'^(?P<pk>\d+)/edit/$', ArticleUpdateView.as_view(), name='article-edit'),
    url(r'^(?P<pk>\d+)/delete/$', ArticleDeleteView.as_view(), name='article-delete'),
    url(r'^(?P<pk>\d+)/publish/$', PublishedArticle, name='article-publish'),
    url(r'^(?P<pk>\d+)/publish/rdf$', PublishedRdf, name='article-rdf'),
    url(r'^search/', ArticleSearchView.as_view(), name='article-search'),
    url(r'^list/', ArticleListView.as_view(), name='article-list'),
    url(r'^menu/', Menu, name='menu'),
]
