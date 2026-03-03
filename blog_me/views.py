from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import *
from django.db.models import Q

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



def posts_by_category(request, category_id, category_slug=None):
    """Show posts for a category identified by its numeric id and optional slug.

    The slug is only used for prettier URLs; if it doesn't match the stored
    value we redirect to the canonical URL.  This also covers the case where
    an old category lacked a slug (``None``) by generating one on the fly.
    """
    category = get_object_or_404(Category, id=category_id)
    # ensure slug exists on the object (populate if blank/null)
    if not category.slug:
        from django.utils.text import slugify
        category.slug = slugify(category.category_names)
        category.save(update_fields=["slug"])
    # if provided slug doesn't match, redirect to the correct URL
    if category_slug != category.slug:
        return redirect(
            'posts_by_category',
            category_id=category.id,
            category_slug=category.slug,
        )
    posts = Blog.objects.filter(category=category, status='Published').order_by('update_at')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'post_by_category.html', context)


def blog_details(request, blog_slug):
    try:
        blog_post = Blog.objects.get(slug=blog_slug, status='Published')
    except Blog.DoesNotExist:
        raise Http404('Blog not found')
    context = {'blog_post': blog_post}
    return render(request, 'blog_details.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
  
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search_blog.html', context)