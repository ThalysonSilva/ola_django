from django.contrib import admin
from django.urls import path
from home import views as home_views

app_name = "home"

urlpatterns = [
    path('', home_views.home, name='home'), # codigo para tela home, ou seja, quando colocar o ip vai aparecer oq tem nessa função citada
]