from django.contrib import admin
from .models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_display = ['title', 'category', 'author','is_featured', 'status', 'create_at', 'update_at']
  search_fields = ('id', 'title' ,'category__category_names', 'status',)
  list_editable = ('is_featured', 'status') 
  list_filter = ('status', 'category', 'author')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
