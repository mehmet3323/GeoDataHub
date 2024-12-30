class GeoAnalyzer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeoAnalyzer, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.cache = {}

    def analyze_water_levels(self, city_data):
        if city_data["adi"] in self.cache:
            return self.cache[city_data["adi"]]

        analysis = {
            "status": "Normal" if city_data["doluluk_orani"] > 50 else "Kritik",
            "trend": self._calculate_trend(city_data),
            "last_updated": datetime.now().isoformat()
        }
        
        self.cache[city_data["adi"]] = analysis
        return analysis

    def _calculate_trend(self, city_data):
        return "stable"  # Örnek implementasyon 