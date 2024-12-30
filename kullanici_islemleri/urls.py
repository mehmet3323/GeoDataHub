from django.contrib import admin
from django.urls import path
from . import views
from .core.patterns.singleton.geo_analyzer import GeoAnalyzer
from .core.patterns.observer.event_manager import EventManager

# Observer Pattern için event handler'ları tanımlayalım
def log_critical_water_level(data):
    print(f"KRİTİK UYARI: {data['city']} şehrinde su seviyesi kritik seviyede!")
    print(f"Seviye: {data['level']}%")
    print(f"Zaman: {data['timestamp']}")

# Event listener'ları kaydedelim
EventManager.subscribe("critical_water_level", log_critical_water_level)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('haberler/', views.haberler, name='haberler'),
    path('sehirler/', views.sehirler, name='sehirler'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('havaKalitesi/', views.havaKalitesi, name='havaKalitesi'),
    path('api/su-doluluk/', views.su_doluluk_api, name='su_doluluk_api'),
]
