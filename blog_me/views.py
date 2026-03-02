from django.shortcuts import render, redirect
from .models import Category, Blog
from django.http import HttpResponse

def home(request):
  featured_posts = Blog.objects.filter(is_featured=True).order_by('update_at')
  posts = Blog.objects.filter(is_featured=False ,status='Published').order_by('update_at')
  
  
  context = {
    'featured_posts': featured_posts,
    'posts': posts,
    
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