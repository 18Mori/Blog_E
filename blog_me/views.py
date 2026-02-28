from django.shortcuts import render
from .models import Category, Blog


def home(request):
  categories = Category.objects.all()
  featured_posts = Blog.objects.filter(is_featured=True).order_by('update_at')
  posts = Blog.objects.filter(is_featured=False ,status='Published').order_by('update_at')
  
  
  context = {
    'categories': categories,
    'featured_posts': featured_posts,
    'posts': posts,
    
  }
  return render(request, 'Home.html', context)
