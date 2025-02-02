from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category


def posts_by_category(request, category_id):
    
    # so use try/except blocks when you wanted to redirect to the home page if there was no blogs. 

    #  unless you can use the get 404 error to show that you don't have that blogs like no post found in this category!
    
    # try:
        
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')

    # fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'posts_by_category.html', context)






