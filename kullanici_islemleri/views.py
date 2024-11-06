from django.shortcuts import render
from .models import Veri

def home(request):
    return render(request, 'home.html')