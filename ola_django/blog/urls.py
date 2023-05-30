from django.contrib import admin
from django.urls import path
from blog import views 

app_name = "blog"

urlpatterns = [
    path('', views.blog, name='home'), # codigo para tela home, ou seja, quando colocar o ip vai aparecer oq tem nessa função citada
    path('post/<int:post_id>/', views.post, name='post'), 
    path('exemplo/', views.exemplo, name='exemplo')
]