"""
URL configuration for awkpedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import create_article, get_article, edit_article, get_article_versions, search_article

urlpatterns = [
    path('articles/create_article/', create_article),
    path('articles/search/', search_article),
    path('<str:slug>', get_article),
    path('<str:slug>/edit', edit_article),
    path('<str:slug>/version', get_article_versions)
] 
