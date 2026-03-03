from django.db import models
from django.contrib.auth.models import User


class Abouts(models.Model):
  heading = models.CharField(max_length=50, blank=True)
  description = models.TextField(max_length=500)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = 'About'
  
  def __str__(self):
    return self.heading
  
class SocialLinks(models.Model):
  platform = models.CharField(max_length=50)
  url = models.URLField(max_length=200)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = 'SocialLinks'
  
  def __str__(self):
    return self.platform


class Category(models.Model):
  category_names = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = 'Categories'
    
  def __str__(self):
    return self.category_names
  
  def save(self, *args, **kwargs):
    # automatically populate slug from the name if not provided
    if not self.slug and self.category_names:
      from django.utils.text import slugify
      self.slug = slugify(self.category_names)
    super().save(*args, **kwargs)
  

STATUS_CHOICES =(
  ('Draft', 'Draft'),
  ('Published', 'Published'),
)

class Blog(models.Model):
  title = models.CharField(max_length=100, unique=True, blank=True)
  slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  is_featured = models.BooleanField(default=False)
  short_description = models.TextField(max_length=500, blank=True)
  featured_image = models.ImageField(upload_to='uplodes/%Y/%m/%d')
  blog_body = models.TextField(max_length=5000, blank=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  status = models.CharField(choices=STATUS_CHOICES, default='Draft')
  
  def __str__(self):
    return self.title
