from ..core.patterns.singleton.geo_analyzer import GeoAnalyzer
from ..core.patterns.factory.data_provider import DataProviderFactory
from ..core.patterns.observer.event_manager import EventManager

class GeoService:
    def __init__(self):
        self.analyzer = GeoAnalyzer()
        self.data_factory = DataProviderFactory()
        
        # Observer pattern için event subscription
        EventManager.subscribe("kritik_su_seviyesi", self._handle_critical_water_level)

    def get_water_data(self, city):
        provider = self.data_factory.create_provider("su")
        data = provider.get_data()
        
        for city_data in data["data"]:
            if city_data["sehir"] == city:
                analysis = self.analyzer.analyze_location(city_data)
                
                if analysis["status"] == "kritik":
                    EventManager.notify("kritik_su_seviyesi", {
                        "sehir": city,
                        "seviye": city_data["water_level"]
                    })
                
                return {**city_data, "analiz": analysis}
        
        return None

    def _handle_critical_water_level(self, data):
        # Kritik su seviyesi durumunda yapılacak işlemler
        pass
