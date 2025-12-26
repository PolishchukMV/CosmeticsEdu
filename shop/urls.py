from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]