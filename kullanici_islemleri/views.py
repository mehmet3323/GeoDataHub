from django.shortcuts import render
from .models import Veri
def index(request):
    return render(request, 'index.html')

def sehirler(request):
    # Bu listede tüm şehirlerin isimlerini ekleyebilirsiniz
    sehirler_listesi = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya']  # Bu listeyi dinamik yapabilirsiniz
    return render(request, 'sehirler.html', {'sehirler': sehirler_listesi})

def sehir_detay(request, sehir_ad):
    # Geçici veriler (şu an için sabit veriler)
    if sehir_ad == "İstanbul":
        sehir_hava_kalitesi = "İyi"
        sehir_su_doluluk_orani = 75.5
    elif sehir_ad == "Ankara":
        sehir_hava_kalitesi = "Orta"
        sehir_su_doluluk_orani = 60.0
    else:
        sehir_hava_kalitesi = "Bilinmiyor"
        sehir_su_doluluk_orani = 0.0
    
    return render(request, 'sehir_detay.html', {
        'sehir_ad': sehir_ad,
        'sehir_hava_kalitesi': sehir_hava_kalitesi,
        'sehir_su_doluluk_orani': sehir_su_doluluk_orani
    })

def home(request):
    sehirler_listesi = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya']
    return render(request, "home.html", {'sehirler': sehirler_listesi})
    #return render(request, "home.html")
    
def get_sehir_verileri(request):
    sehirler = [
        {"sehir": "Ankara", "lat": 39.9334, "lng": 32.8597, "havaKalitesi": 50, "suDoluluk": 70},
        {"sehir": "İstanbul", "lat": 41.0082, "lng": 28.9784, "havaKalitesi": 60, "suDoluluk": 65}
    ]
    return JsonResponse(sehirler, safe=False)

def haberler(request):
    return render(request, "haberler.html")


def hakkimizda(request):
    return render(request, "hakkimizda.html")
