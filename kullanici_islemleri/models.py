from django.db import models
from django.contrib.auth.models import User

class UserActivity(models.Model):
    ACTIONS = [
        ('add_data', 'Yeni Veri Ekledi'),
        ('update_data', 'Veri Güncelledi'),
        ('delete_data', 'Veri Sildi'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=50, choices=ACTIONS)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} @ {self.timestamp}"

class Region(models.Model):
    name = models.CharField(max_length=255)
    parent_region = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subregions')
    geometry = models.TextField(blank=True, null=True)  # GeoDjango ile PointField veya PolygonField kullanılabilir

    def __str__(self):
        return f"{self.name} ({self.parent_region.name if self.parent_region else 'Root'})"

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
