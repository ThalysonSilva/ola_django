from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request): # O resquest
    print('blog')
    context={
        #'text':'Olá Blog',
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)  #coloca o nome do APP que foi criado que no caso é blog, e depois coloca o nome do arquivo html

def post(request, post_id): 
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post == post
            break

    print('post', post_id)
    context={
        #'text':'Olá Post',
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)  #coloca o nome do APP que foi criado que no caso é blog, e depois coloca o nome do arquivo html

def exemplo(request): # O resquest
    print('exemplo')
    context={
        #'text':'Olá Exemplo do Blog',
        'posts': posts
    }
    return render(request, 'blog/exemplo.html', context)