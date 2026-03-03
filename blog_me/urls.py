from django.urls import path
from .import views

urlpatterns = [
    # home page under the "category/" prefix
    path('', views.home, name='Home'),
    # search must come before the slug patterns so it isn’t treated as a slug
    path('search/', views.search, name='search'),
    # category pages: accept id alone or id+slug for prettier URLs
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('<int:category_id>/<slug:category_slug>/', views.posts_by_category, name='posts_by_category'),
    path('<slug:blog_slug>/', views.blog_details, name='blog_details'),
]