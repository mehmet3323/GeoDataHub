"""
URL configuration for Cografi_bilgi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from kullanici_islemleri import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Anasayfa
    path("sehirler/", views.sehirler, name="sehirler"),  # Şehirler sayfası
    path("haberler/", views.haberler, name="haberler"),  # Haberler sayfası
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),  # Hakkımızda sayfası
]

# Statik dosyaların ve medya dosyalarının doğru şekilde sunulabilmesi için eklemeler
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
