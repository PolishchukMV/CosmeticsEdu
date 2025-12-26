from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', include('django.contrib.auth.urls')),  # Добавляет login, logout, password_change и т.д.
]