from django.shortcuts import render, redirect
from .models import *
from user_dashboard.models import *
from django.db.models import Q
from core_blog.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
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
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('Home')

def home(request):
  featured_posts = Blog.objects.filter(is_featured=True).order_by('update_at')
  posts = Blog.objects.filter(is_featured=False ,status='Published').order_by('update_at')
  
  try:
    about = Abouts.objects.get()
  except Abouts.DoesNotExist:
    about = None
    
  context = {
    'featured_posts': featured_posts,
    'posts': posts,
    'about': about,
  }
  return render(request, 'Home.html', context)


def posts_by_category(request, category_id):
  posts =Blog.objects.filter(category=category_id,status='Published').order_by('update_at')
  try:
    category = Category.objects.get(id=category_id)
  except Category.DoesNotExist:
      return redirect('404')
  context = {
    'category' : category,
    'posts' : posts,
  }
  return render(request, 'post_by_category.html', context)


def blog_details(request, blog_slug):
  try:
    blog_post = Blog.objects.get(slug=blog_slug, status='Published')
  except Blog.DoesNotExist:
    return redirect('404')
  context = {
    'blog_post' :blog_post,
  }
  return render(request, 'blog_details.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
  
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search_blog.html', context)