from django.contrib import admin
from django.urls import path
from . import views  # views.py dosyasını dahil ediyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ana sayfa için rota ekliyoruz
]
