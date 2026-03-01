from django.shortcuts import render, get_object_or_404
from .models import Category, Blog
from django.http import HttpResponse

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


def posts_by_category(request, category_id):
  posts =Blog.objects.filter(category=category_id,status='Published').order_by('update_at')
  category = get_object_or_404(Category, id=category_id)
  context = {
    'category' : category,
    'posts' : posts,
  }
  return render(request, 'post_by_category.html', context=context)