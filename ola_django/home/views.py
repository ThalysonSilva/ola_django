#from django.shortcuts import render
from django.shortcuts import render
from home.data import posts

# Create your views here.
def home(request): # O resquest
    print('Home')
    context={
        #'text':'Olá Home',
        'posts': posts
    }
    return render(request, 'home/index.html', context)