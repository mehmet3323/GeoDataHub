from django.shortcuts import render
from django.http import JsonResponse
from .core.patterns.singleton.geo_analyzer import GeoAnalyzer
from .core.patterns.factory.factory.data_provider import DataProviderFactory
from .core.patterns.observer.observer.event_manager import EventManager
from datetime import datetime
from kullanici_islemleri.models import UserActivity

def log_user_action(user, action, details=None):
    UserActivity.objects.create(user=user, action=action, details=details)
class BaseView:
    def __init__(self):
        self.analyzer = GeoAnalyzer()
        self.data_factory = DataProviderFactory()
        self.event_manager = EventManager()

class HomeView(BaseView):
    def get(self, request):
        return render(request, "home.html")

class SehirlerView(BaseView):
    def get(self, request):
        return render(request, "sehirler.html")

class HaberlerView(BaseView):
    def get(self, request):
        return render(request, "haberler.html")

class HakkimizdaView(BaseView):
    def get(self, request):
        return render(request, "hakkimizda.html")

class HavaKalitesiView(BaseView):
    def get(self, request):
        return render(request, "havaKalitesi.html")

class SuDolulukAPIView(BaseView):
    def get(self, request):
        try:
            # Factory Pattern kullanımı
            water_provider = self.data_factory.create_provider("water")
            data = water_provider.get_data()
            
            # Singleton Pattern kullanımı
            for city in data:
                analysis = self.analyzer.analyze_water_levels(city)
                city["analysis"] = analysis
                
                # Observer Pattern kullanımı
                if analysis["status"] == "Kritik":
                    self.event_manager.notify("critical_water_level", {
                        "city": city["adi"],
                        "level": city["doluluk_orani"],
                        "timestamp": datetime.now().isoformat()
                    })
            
            return JsonResponse(data, safe=False)
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
class HaberlerView(BaseView):
    def get(self, request):
        category = request.GET.get('category', 'all')
        
        haberler = [
            {
                'id': 1,
                'title': 'Türkiye\'nin Su Kaynakları Raporu Yayınlandı',
                'description': 'DSİ tarafından hazırlanan 2024 yılı su kaynakları raporuna göre, ülkemizdeki barajların ortalama doluluk oranı %65 seviyesinde seyrediyor.',
                'full_content': 'DSİ tarafından hazırlanan 2024 yılı su kaynakları raporuna göre...',
                'date': '20 Mart 2024',
                'source': 'Devlet Su İşleri',
                'source_url': 'https://www.dsi.gov.tr/Sayfa/Detay/1322',
                'category': 'Su Kaynakları'
            },
            {
                'id': 2,
                'title': 'İklim Değişikliği Su Kaynaklarını Tehdit Ediyor',
                'description': 'Türkiye\'de iklim değişikliğinin etkileri su kaynakları üzerinde ciddi baskı oluşturuyor.',
                'full_content': 'İklim değişikliğinin etkileri giderek artıyor...',
                'date': '19 Mart 2024',
                'source': 'İklim Araştırmaları Merkezi',
                'source_url': 'https://www.mgm.gov.tr/iklim/iklim-degisikligi.aspx',
                'category': 'İklim'
            },
            {
                'id': 3,
                'title': 'Akıllı Su Yönetimi Projeleri Başlıyor',
                'description': '5 büyükşehirde akıllı su yönetimi projeleri hayata geçiriliyor.',
                'full_content': 'Akıllı su yönetimi projeleri kapsamında...',
                'date': '18 Mart 2024',
                'source': 'Çevre Bakanlığı',
                'source_url': 'https://www.csb.gov.tr/projeler/su-yonetimi',
                'category': 'Projeler'
            },
            {
                'id': 4,
                'title': 'Küresel Su Krizi Derinleşiyor',
                'description': 'BM raporuna göre, dünya nüfusunun üçte biri temiz suya erişimde zorluk yaşıyor.',
                'full_content': 'Birleşmiş Milletler\'in son raporuna göre...',
                'date': '17 Mart 2024',
                'source': 'Birleşmiş Milletler',
                'source_url': 'https://www.un.org/water/reports',
                'category': 'Küresel'
            },
            {
                'id': 5,
                'title': 'Akdeniz\'de Su Stresi Alarm Veriyor',
                'description': 'Akdeniz havzasında artan sıcaklıklar ve azalan yağışlar nedeniyle su stresi kritik seviyelere ulaştı.',
                'full_content': 'Akdeniz Bölgesi\'nde su kaynaklarının durumu...',
                'date': '16 Mart 2024',
                'source': 'Akdeniz İklim Değişikliği Merkezi',
                'source_url': 'https://www.akdeniziklim.org/raporlar',
                'category': 'Su Kaynakları'
            },
            {
                'id': 6,
                'title': 'Yeni Nesil Su Arıtma Teknolojileri',
                'description': 'Nanoteknoloji kullanılarak geliştirilen yeni su arıtma sistemleri test ediliyor.',
                'full_content': 'Yeni nesil su arıtma teknolojileri ile...',
                'date': '15 Mart 2024',
                'source': 'Teknoloji Araştırma Merkezi',
                'source_url': 'https://www.tubitak.gov.tr/su-teknolojileri',
                'category': 'Projeler'
            },
            {
                'id': 7,
                'title': 'Kar Yağışları Azalıyor',
                'description': 'Son 50 yılın kar yağışı verileri endişe verici bir tablo ortaya koyuyor.',
                'full_content': 'Meteoroloji Genel Müdürlüğü verilerine göre...',
                'date': '14 Mart 2024',
                'source': 'Meteoroloji Genel Müdürlüğü',
                'source_url': 'https://www.mgm.gov.tr/veridegerlendirme/kar-analizi.aspx',
                'category': 'İklim'
            },
            {
                'id': 8,
                'title': 'Su Tasarrufu Kampanyası Başlatıldı',
                'description': 'Büyükşehir belediyeleri ortak su tasarrufu kampanyası başlattı.',
                'full_content': 'Su tasarrufu kampanyası kapsamında...',
                'date': '13 Mart 2024',
                'source': 'Belediyeler Birliği',
                'source_url': 'https://www.tbb.gov.tr/su-tasarrufu-kampanyasi',
                'category': 'Projeler'
            },
            {
                'id': 9,
                'title': 'Yeraltı Suları Tehlike Altında',
                'description': 'Aşırı kullanım nedeniyle yeraltı su seviyeleri kritik seviyelere indi.',
                'full_content': 'Yeraltı su kaynaklarının durumu...',
                'date': '12 Mart 2024',
                'source': 'DSİ',
                'source_url': 'https://www.dsi.gov.tr/yeralti-sulari-raporu',
                'category': 'Su Kaynakları'
            },
            {
                'id': 10,
                'title': 'Dünya Su Günü Etkinlikleri',
                'description': '22 Mart Dünya Su Günü kapsamında çeşitli etkinlikler düzenlenecek.',
                'full_content': 'Dünya Su Günü etkinlikleri çerçevesinde...',
                'date': '11 Mart 2024',
                'source': 'Çevre Bakanlığı',
                'source_url': 'https://www.csb.gov.tr/dunya-su-gunu-2024',
                'category': 'Küresel'
            }
        ]
        
        if category != 'all':
            haberler = [haber for haber in haberler if haber['category'].lower() == category.lower()]
            
        return render(request, 'haberler.html', {'haberler': haberler})

    def get_haber_detail(self, request, haber_id):
        # get_haber_detail metodunda da aynı haberlerin detayları olmalı
        haberler = {
            # Mevcut 4 haber detayı aynen kalacak...
            5: {
                'title': 'Akdeniz\'de Su Stresi Alarm Veriyor',
                'full_content': '''[Akdeniz su stresi haberinin tam içeriği]''',
                'date': '16 Mart 2024',
                'source': 'Akdeniz İklim Değişikliği Merkezi',
                'category': 'Su Kaynakları'
            },
            # 5 yeni haber detayı daha eklenecek...
        }
        
        haber = haberler.get(haber_id)
        if haber:
            return JsonResponse(haber)
        return JsonResponse({'error': 'Haber bulunamadı'}, status=404)

# Function-based views
def home(request):
    return HomeView().get(request)

def sehirler(request):
    return SehirlerView().get(request)

def haberler(request):
    return HaberlerView().get(request)

def hakkimizda(request):
    return HakkimizdaView().get(request)

def havaKalitesi(request):
    return HavaKalitesiView().get(request)



# Su doluluk API endpoint
def su_doluluk_api(request):
    sehirler_data = [
        {
            "adi": "İstanbul",
            "latitude": 41.0082,
            "longitude": 28.9784,
            "doluluk_orani": 65.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Ömerli Barajı", "oran": 68.5},
                {"ad": "Sazlıdere Barajı", "oran": 62.3},
                {"ad": "Büyükçekmece Barajı", "oran": 66.7}
            ]
        },
        {
            "adi": "Ankara",
            "latitude": 39.9334,
            "longitude": 32.8597,
            "doluluk_orani": 45.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Çamlıdere Barajı", "oran": 42.8},
                {"ad": "Kurtboğazı Barajı", "oran": 47.6}
            ]
        },
        {
            "adi": "İzmir",
            "latitude": 38.4189,
            "longitude": 27.1287,
            "doluluk_orani": 78.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Tahtalı Barajı", "oran": 82.1},
                {"ad": "Balçova Barajı", "oran": 74.7}
            ]
        },
        {
            "adi": "Bursa",
            "latitude": 40.1885,
            "longitude": 29.0610,
            "doluluk_orani": 72.5,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Doğancı Barajı", "oran": 75.3},
                {"ad": "Nilüfer Barajı", "oran": 69.7}
            ]
        },
        {
            "adi": "Antalya",
            "latitude": 36.8969,
            "longitude": 30.7133,
            "doluluk_orani": 85.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Oymapınar Barajı", "oran": 88.2},
                {"ad": "Alakır Barajı", "oran": 82.4}
            ]
        },
        {
            "adi": "Adana",
            "latitude": 37.0000,
            "longitude": 35.3213,
            "doluluk_orani": 68.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Seyhan Barajı", "oran": 71.2},
                {"ad": "Çatalan Barajı", "oran": 66.6}
            ]
        },
        {
            "adi": "Konya",
            "latitude": 37.8667,
            "longitude": 32.4833,
            "doluluk_orani": 48.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Altınapa Barajı", "oran": 51.2},
                {"ad": "Beyşehir Gölü", "oran": 46.6}
            ]
        },
        {
            "adi": "Gaziantep",
            "latitude": 37.0662,
            "longitude": 37.3833,
            "doluluk_orani": 55.6,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kartalkaya Barajı", "oran": 57.9},
                {"ad": "Hancağız Barajı", "oran": 53.3}
            ]
        },
        {
            "adi": "Şanlıurfa",
            "latitude": 37.1591,
            "longitude": 38.7969,
            "doluluk_orani": 52.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Atatürk Barajı", "oran": 54.6},
                {"ad": "Birecik Barajı", "oran": 50.2}
            ]
        },
        {
            "adi": "Mersin",
            "latitude": 36.8000,
            "longitude": 34.6333,
            "doluluk_orani": 67.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Berdan Barajı", "oran": 70.1},
                {"ad": "Pamukluk Barajı", "oran": 65.5}
            ]
        },
        {
            "adi": "Kayseri",
            "latitude": 38.7312,
            "longitude": 35.4787,
            "doluluk_orani": 59.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Yamula Barajı", "oran": 61.7},
                {"ad": "Bahçelik Barajı", "oran": 57.1}
            ]
        },
        {
            "adi": "Diyarbakır",
            "latitude": 37.9144,
            "longitude": 40.2306,
            "doluluk_orani": 58.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Dicle Barajı", "oran": 60.7},
                {"ad": "Kralkızı Barajı", "oran": 56.1}
            ]
        },
        {
            "adi": "Eskişehir",
            "latitude": 39.7767,
            "longitude": 30.5206,
            "doluluk_orani": 67.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Porsuk Barajı", "oran": 69.6},
                {"ad": "Gökçekaya Barajı", "oran": 65.0}
            ]
        },
        {
            "adi": "Samsun",
            "latitude": 41.2867,
            "longitude": 36.3300,
            "doluluk_orani": 69.5,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Derbent Barajı", "oran": 71.8},
                {"ad": "Çakmak Barajı", "oran": 67.2}
            ]
        },
        {
            "adi": "Denizli",
            "latitude": 37.7765,
            "longitude": 29.0864,
            "doluluk_orani": 66.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Gökpınar Barajı", "oran": 69.2},
                {"ad": "Cindere Barajı", "oran": 64.4}
            ]
        },
        {
            "adi": "Kahramanmaraş",
            "latitude": 37.5858,
            "longitude": 36.9371,
            "doluluk_orani": 59.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kartalkaya Barajı", "oran": 62.1},
                {"ad": "Ayvalı Barajı", "oran": 57.5}
            ]
        },
        {
            "adi": "Malatya",
            "latitude": 38.3552,
            "longitude": 38.3095,
            "doluluk_orani": 61.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Çat Barajı", "oran": 64.0},
                {"ad": "Kapıkaya Barajı", "oran": 59.4}
            ]
        },
        {
            "adi": "Hatay",
            "latitude": 36.4018,
            "longitude": 36.3498,
            "doluluk_orani": 63.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Yarseli Barajı", "oran": 65.9},
                {"ad": "Tahtaköprü Barajı", "oran": 61.5}
            ]
        },
        {
            "adi": "Balıkesir",
            "latitude": 39.6484,
            "longitude": 27.8826,
            "doluluk_orani": 59.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Manyas Barajı", "oran": 57.4},
                {"ad": "Çaygören Barajı", "oran": 61.0}
            ]
        },
        {
            "adi": "Van",
            "latitude": 38.4891,
            "longitude": 43.4089,
            "doluluk_orani": 61.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Koçköprü Barajı", "oran": 63.4},
                {"ad": "Hoşap Barajı", "oran": 59.0}
            ]
        },
        {
            "adi": "Tekirdağ",
            "latitude": 40.9833,
            "longitude": 27.5167,
            "doluluk_orani": 66.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Şarköy Barajı", "oran": 68.7},
                {"ad": "Naipköy Barajı", "oran": 64.1}
            ]
        },
        {
            "adi": "Aydın",
            "latitude": 37.8444,
            "longitude": 27.8458,
            "doluluk_orani": 63.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kemer Barajı", "oran": 65.8},
                {"ad": "İkizdere Barajı", "oran": 61.6}
            ]
        },
        {
            "adi": "Manisa",
            "latitude": 38.6191,
            "longitude": 27.4289,
            "doluluk_orani": 65.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Demirköprü Barajı", "oran": 68.1},
                {"ad": "Gördes Barajı", "oran": 63.5}
            ]
        },
        {
            "adi": "Trabzon",
            "latitude": 41.0015,
            "longitude": 39.7178,
            "doluluk_orani": 79.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Atasu Barajı", "oran": 81.5},
                {"ad": "Şenel Barajı", "oran": 77.1}
            ]
        },
        {
            "adi": "Muğla",
            "latitude": 37.2153,
            "longitude": 28.3636,
            "doluluk_orani": 71.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Mumcular Barajı", "oran": 73.7},
                {"ad": "Geyik Barajı", "oran": 69.1}
            ]
        },
        {
            "adi": "Sakarya",
            "latitude": 40.7569,
            "longitude": 30.3781,
            "doluluk_orani": 68.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Sapanca Gölü", "oran": 71.2},
                {"ad": "Akgöl Barajı", "oran": 66.6}
            ]
        },
        {
            "adi": "Erzurum",
            "latitude": 39.9000,
            "longitude": 41.2700,
            "doluluk_orani": 59.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Palandöken Barajı", "oran": 62.1},
                {"ad": "Çat Barajı", "oran": 57.5}
            ]
        },
        {
            "adi": "Ordu",
            "latitude": 40.9839,
            "longitude": 37.8764,
            "doluluk_orani": 71.6,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kürtün Barajı", "oran": 73.9},
                {"ad": "Topçam Barajı", "oran": 69.3}
            ]
        },
        {
            "adi": "Kocaeli",
            "latitude": 40.8533,
            "longitude": 29.8815,
            "doluluk_orani": 73.6,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Yuvacık Barajı", "oran": 75.9},
                {"ad": "Namazgah Barajı", "oran": 71.3}
            ]
        },
        {
            "adi": "Kütahya",
            "latitude": 39.4167,
            "longitude": 29.9833,
            "doluluk_orani": 62.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Porsuk Barajı", "oran": 64.6},
                {"ad": "Kayaboğazı Barajı", "oran": 60.0}
            ]
        },
        {
            "adi": "Çanakkale",
            "latitude": 40.1553,
            "longitude": 26.4142,
            "doluluk_orani": 64.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Atikhisar Barajı", "oran": 66.3},
                {"ad": "Bayramiç Barajı", "oran": 63.1}
            ]
        },
        {
            "adi": "Sivas",
            "latitude": 39.7477,
            "longitude": 37.0179,
            "doluluk_orani": 61.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "4 Eylül Barajı", "oran": 63.9},
                {"ad": "Pusat-Özen Barajı", "oran": 59.7}
            ]
        },
        {
            "adi": "Tokat",
            "latitude": 40.3167,
            "longitude": 36.5500,
            "doluluk_orani": 64.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Almus Barajı", "oran": 67.2},
                {"ad": "Güzelce Barajı", "oran": 62.6}
            ]
        },
        {
            "adi": "Afyonkarahisar",
            "latitude": 38.7568,
            "longitude": 30.5387,
            "doluluk_orani": 45.6,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Selevir Barajı", "oran": 43.2},
                {"ad": "Çay Barajı", "oran": 48.0}
            ]
        },
        {
            "adi": "Yozgat",
            "latitude": 39.8181,
            "longitude": 34.8147,
            "doluluk_orani": 56.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Gelingüllü Barajı", "oran": 59.2},
                {"ad": "Uzunlu Barajı", "oran": 54.6}
            ]
        },
        {
            "adi": "Elazığ",
            "latitude": 38.6810,
            "longitude": 39.2264,
            "doluluk_orani": 64.5,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Keban Barajı", "oran": 66.8},
                {"ad": "Karakaya Barajı", "oran": 62.2}
            ]
        },
        {
            "adi": "Zonguldak",
            "latitude": 41.4564,
            "longitude": 31.7987,
            "doluluk_orani": 68.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kozlu Barajı", "oran": 70.5},
                {"ad": "Ulutan Barajı", "oran": 66.1}
            ]
        },
        {
            "adi": "Adıyaman",
            "latitude": 37.7648,
            "longitude": 38.2786,
            "doluluk_orani": 57.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Çamgazi Barajı", "oran": 55.4},
                {"ad": "Gömükan Barajı", "oran": 60.2}
            ]
        },
        {
            "adi": "Osmaniye",
            "latitude": 37.0742,
            "longitude": 36.2463,
            "doluluk_orani": 62.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kalecik Barajı", "oran": 64.5},
                {"ad": "Bahçe Barajı", "oran": 60.1}
            ]
        },
        {
            "adi": "Kırklareli",
            "latitude": 41.7333,
            "longitude": 27.2167,
            "doluluk_orani": 70.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Armağan Barajı", "oran": 72.5},
                {"ad": "Kırklareli Barajı", "oran": 67.9}
            ]
        },
        {
            "adi": "Edirne",
            "latitude": 41.6771,
            "longitude": 26.5557,
            "doluluk_orani": 71.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Süloğlu Barajı", "oran": 73.5},
                {"ad": "Altınyazı Barajı", "oran": 68.9}
            ]
        },
        {
            "adi": "Ağrı",
            "latitude": 39.7191,
            "longitude": 43.0566,
            "doluluk_orani": 62.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Yazıcı Barajı", "oran": 64.5},
                {"ad": "Patnos Barajı", "oran": 60.1}
            ]
        },
        {
            "adi": "Ardahan",
            "latitude": 41.1105,
            "longitude": 42.7022,
            "doluluk_orani": 61.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Çıldır Gölü", "oran": 63.6},
                {"ad": "Aktaş Gölü", "oran": 59.2}
            ]
        },
        {
            "adi": "Artvin",
            "latitude": 41.1828,
            "longitude": 41.8183,
            "doluluk_orani": 75.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Borçka Barajı", "oran": 78.3},
                {"ad": "Deriner Barajı", "oran": 72.5}
            ]
        },
        {
            "adi": "Bingöl",
            "latitude": 38.8854,
            "longitude": 40.4983,
            "doluluk_orani": 58.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Gayt Barajı", "oran": 60.9},
                {"ad": "Kiğı Barajı", "oran": 56.5}
            ]
        },
        {
            "adi": "Bitlis",
            "latitude": 38.4006,
            "longitude": 42.1095,
            "doluluk_orani": 64.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Ahlat Barajı", "oran": 66.5},
                {"ad": "Kotum Barajı", "oran": 61.9}
            ]
        },
        {
            "adi": "Erzincan",
            "latitude": 39.7500,
            "longitude": 39.5000,
            "doluluk_orani": 62.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Tercan Barajı", "oran": 64.9},
                {"ad": "Girlevik Barajı", "oran": 60.5}
            ]
        },
        {
            "adi": "Hakkari",
            "latitude": 37.5744,
            "longitude": 43.7408,
            "doluluk_orani": 58.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Dilimli Barajı", "oran": 61.2},
                {"ad": "Zernek Barajı", "oran": 56.6}
            ]
        },
        {
            "adi": "Iğdır",
            "latitude": 39.9167,
            "longitude": 44.0333,
            "doluluk_orani": 56.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Serdarabat Barajı", "oran": 59.0},
                {"ad": "Aras Barajı", "oran": 54.6}
            ]
        },
        {
            "adi": "Kars",
            "latitude": 40.6167,
            "longitude": 43.1000,
            "doluluk_orani": 57.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kars Barajı", "oran": 60.1},
                {"ad": "Çıldır Gölü", "oran": 55.5}
            ]
        },
        {
            "adi": "Muş",
            "latitude": 38.7432,
            "longitude": 41.5064,
            "doluluk_orani": 59.6,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Alparslan Barajı", "oran": 61.9},
                {"ad": "Varto Barajı", "oran": 57.3}
            ]
        },
        {
            "adi": "Siirt",
            "latitude": 37.9333,
            "longitude": 41.9500,
            "doluluk_orani": 56.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Alkumru Barajı", "oran": 58.9},
                {"ad": "Kayser Barajı", "oran": 54.5}
            ]
        },
        {
            "adi": "Şırnak",
            "latitude": 37.5164,
            "longitude": 42.4611,
            "doluluk_orani": 55.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Silopi Barajı", "oran": 57.9},
                {"ad": "Cizre Barajı", "oran": 53.7}
            ]
        },
        {
            "adi": "Tunceli",
            "latitude": 39.1079,
            "longitude": 39.5401,
            "doluluk_orani": 63.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Uzunçayır Barajı", "oran": 65.9},
                {"ad": "Tatar Barajı", "oran": 61.5}
            ]
        },
        {
            "adi": "Rize",
            "latitude": 41.0201,
            "longitude": 40.5234,
            "doluluk_orani": 82.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "İkizdere Barajı", "oran": 84.7},
                {"ad": "Çayeli Barajı", "oran": 80.1}
            ]
        },
        {
            "adi": "Giresun",
            "latitude": 40.9128,
            "longitude": 38.3895,
            "doluluk_orani": 73.4,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Aksu Barajı", "oran": 75.7},
                {"ad": "Dereli Barajı", "oran": 71.1}
            ]
        },
        {
            "adi": "Gümüşhane",
            "latitude": 40.4386,
            "longitude": 39.5086,
            "doluluk_orani": 65.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Torul Barajı", "oran": 67.5},
                {"ad": "Kürtün Barajı", "oran": 62.9}
            ]
        },
        {
            "adi": "Bartın",
            "latitude": 41.6344,
            "longitude": 32.3375,
            "doluluk_orani": 69.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kirazlıköprü Barajı", "oran": 71.9},
                {"ad": "Kozcağız Barajı", "oran": 67.5}
            ]
        },
        {
            "adi": "Kastamonu",
            "latitude": 41.3887,
            "longitude": 33.7827,
            "doluluk_orani": 68.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Karaçomak Barajı", "oran": 71.2},
                {"ad": "Germeçtepe Barajı", "oran": 66.6}
            ]
        },
        {
            "adi": "Sinop",
            "latitude": 42.0231,
            "longitude": 35.1531,
            "doluluk_orani": 73.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Erfelek Barajı", "oran": 75.4},
                {"ad": "Boyabat Barajı", "oran": 71.0}
            ]
        },
        {
            "adi": "Çorum",
            "latitude": 40.5499,
            "longitude": 34.9537,
            "doluluk_orani": 61.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Obruk Barajı", "oran": 63.9},
                {"ad": "Yenihayat Barajı", "oran": 59.7}
            ]
        },
        {
            "adi": "Amasya",
            "latitude": 40.6499,
            "longitude": 35.8353,
            "doluluk_orani": 58.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Yedikır Barajı", "oran": 61.2},
                {"ad": "Derinöz Barajı", "oran": 56.6}
            ]
        },
        {
            "adi": "Karabük",
            "latitude": 41.2061,
            "longitude": 32.6204,
            "doluluk_orani": 64.5,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Soğanlı Barajı", "oran": 66.8},
                {"ad": "Kızılkaya Barajı", "oran": 62.2}
            ]
        },
        {
            "adi": "Düzce",
            "latitude": 40.8438,
            "longitude": 31.1565,
            "doluluk_orani": 71.3,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Hasanlar Barajı", "oran": 73.5},
                {"ad": "Akçay Barajı", "oran": 69.1}
            ]
        },
        {
            "adi": "Bolu",
            "latitude": 40.7339,
            "longitude": 31.6082,
            "doluluk_orani": 67.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Gölköy Barajı", "oran": 70.1},
                {"ad": "Yumrukaya Barajı", "oran": 65.5}
            ]
        },
        {
            "adi": "Çankırı",
            "latitude": 40.6013,
            "longitude": 33.6134,
            "doluluk_orani": 55.9,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Güldürcek Barajı", "oran": 57.2},
                {"ad": "Demirçevre Barajı", "oran": 54.6}
            ]
        },
        {
            "adi": "Kırıkkale",
            "latitude": 39.8468,
            "longitude": 33.5153,
            "doluluk_orani": 57.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Kapulukaya Barajı", "oran": 59.4},
                {"ad": "Kesikköprü Barajı", "oran": 55.0}
            ]
        },
        {
            "adi": "Kırşehir",
            "latitude": 39.1425,
            "longitude": 34.1709,
            "doluluk_orani": 56.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Hirfanlı Barajı", "oran": 59.0},
                {"ad": "Kültepe Barajı", "oran": 54.4}
            ]
        },
        {
            "adi": "Nevşehir",
            "latitude": 38.6244,
            "longitude": 34.7239,
            "doluluk_orani": 57.2,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Damsa Barajı", "oran": 59.4},
                {"ad": "Tatlarin Barajı", "oran": 55.0}
            ]
        },
        {
            "adi": "Niğde",
            "latitude": 37.9667,
            "longitude": 34.6833,
            "doluluk_orani": 54.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Gebere Barajı", "oran": 56.5},
                {"ad": "Akkaya Barajı", "oran": 53.1}
            ]
        },
        {
            "adi": "Aksaray",
            "latitude": 38.3687,
            "longitude": 34.0370,
            "doluluk_orani": 53.7,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Mamasın Barajı", "oran": 55.9},
                {"ad": "Kültepe Barajı", "oran": 51.5}
            ]
        },
        {
            "adi": "Karaman",
            "latitude": 37.1759,
            "longitude": 33.2287,
            "doluluk_orani": 55.8,
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "barajlar": [
                {"ad": "Ermenek Barajı", "oran": 57.9},
                {"ad": "İbrala Barajı", "oran": 53.7}
            ]
        }
    ]
    return JsonResponse(sehirler_data, safe=False)

