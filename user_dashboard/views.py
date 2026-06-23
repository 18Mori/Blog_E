from django.shortcuts import render, redirect, get_object_or_404
from blog_me.models import *
from django.contrib.auth.decorators import login_required
from .user_forms import *

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard.html', context)

def categories(request):
    return render(request, 'categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)
