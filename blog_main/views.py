
from django.shortcuts import redirect, render

from blogs.models import Blog, Category
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
            
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context) 

def logout(request):
    auth.logout(request)
    return redirect('home')