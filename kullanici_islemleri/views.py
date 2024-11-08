from django.shortcuts import render
from .models import Veri


from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def sehirler(request):
    return render(request, "sehirler.html")


def haberler(request):
    return render(request, "haberler.html")


def hakkimizda(request):
    return render(request, "hakkimizda.html")
