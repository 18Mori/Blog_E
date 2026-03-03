from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('<slug:blog_slug>/', views.blog_details, name='blog_details')
]