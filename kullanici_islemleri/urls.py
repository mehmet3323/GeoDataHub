from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ana sayfa rotası
    path('get_sehir_verileri/', views.get_sehir_verileri, name='get_sehir_verileri'),
    #path('sehirler/', views.sehirler, name='sehirler'),  # Şehirler sayfası
    #path('sehirler/<str:sehir_ad>/', views.sehir_detay, name='sehir_detay'),  # Seçilen şehir detay sayfası
    path('haberler/', views.haberler, name='haberler'),  # Haberler sayfası
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),  # Hakkımızda sayfası
]

