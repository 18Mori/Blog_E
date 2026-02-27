from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  category_names = models.CharField(max_length=100, unique=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = 'Categories'
    
  def __str__(self):
    return self.category_names
  

STATUS_CHOICES =(
  (0, 'Draft'),
  (1, 'Published'),
)

class Blog(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, unique=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  auther = models.ForeignKey(User, on_delete=models.CASCADE)
  is_featured = models.BooleanField(default=False)
  short_description = models.TextField(max_length=100)
  featured_image = models.ImageField(upload_to='uplodes/%Y/%m/%d')
  blog_body = models.TextField(max_length=5000)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS_CHOICES, default=0)
  
  def __str__(self):
    return self.title
