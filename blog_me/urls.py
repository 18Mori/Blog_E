from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='Home'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('<slug:blog_slug>/', views.blog_details, name='blog_details'),
]