from django.db import models
from django.contrib.auth.models import User

class Veri(models.Model):
    veri_tipi = models.CharField(max_length=50)  # örn. Su Doluluk, Hava Kirliliği
    tarih = models.DateTimeField(auto_now_add=True)
    deger = models.FloatField()

class Haber(models.Model):
    baslik = models.CharField(max_length=255)
    icerik = models.TextField()
    yayin_tarihi = models.DateField()

class Uyari(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    mesaj = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

class Sehir(models.Model):
    adi = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    aqi = models.IntegerField(null=True, blank=True)  # Hava kalitesi verisi

    def __str__(self):
        return self.adi
