from django.shortcuts import render
from .models import Veri

def veri_goruntule(request):
    veriler = Veri.objects.all()
    return render(request, 'veri_yonetimi/veri_goruntule.html', {'veriler': veriler})