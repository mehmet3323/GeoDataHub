from django.shortcuts import render
import requests


# Home page view
def home(request):
    return render(request, "home.html")


# Sehirler page view
def sehirler(request):
    return render(request, "sehirler.html")


# Haberler page view
def haberler(request):
    return render(request, "haberler.html")


# Hakkımızda page view
def hakkimizda(request):
    return render(request, "hakkimizda.html")
