from django.contrib import admin
from django.urls import path
from . import views  # views.py dosyasını dahil ediyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ana sayfa için rota
    path('haberler/', views.haberler_view, name='haberler'),  # Haberler için rota
    path('sehirler/', views.sehirler, name='sehirler'),  # Şehirler için rota
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),  # Hakkımızda için rota
    path('havaKalitesi/', views.havaKalitesi, name='havaKalitesi'),  # Hakkımızda için rota
    path('api/su-doluluk/', views.su_doluluk_api, name='su_doluluk_api'),
]
