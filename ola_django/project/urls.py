"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include


# HTTP Resquest <-> HTTP Response

#Urls
# Regra básica, nenhuma das URL vai começar com barra(/).
urlpatterns = [
    path('', include('home.urls')), # codigo para tela home, ou seja, quando colocar o ip vai aparecer oq tem nessa função citada
    path('blog/', include('blog.urls')), # esse foi feito manual como configurar um novo url, precisa ter o resquest e o response
    path('admin/', admin.site.urls) # esse já vem como o django incluso
]
