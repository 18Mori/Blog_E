from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('<int:category_id>/', views.posts_by_category, name='post_by_category')
]