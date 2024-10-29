import requests
from .models import Veri

def veri_cek(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            Veri.objects.create(
                veri_tipi=item["type"],
                tarih=item["date"],
                deger=item["value"]
            )