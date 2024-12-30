from abc import ABC, abstractmethod

class DataProvider(ABC):
    @abstractmethod
    def get_data(self):
        pass

class WaterDataProvider(DataProvider):
    def get_data(self):
        # Örnek veri
        return [
            {
                "adi": "İstanbul",
                "doluluk_orani": 65.8,
                "barajlar": [
                    {"ad": "Ömerli Barajı", "oran": 68.5},
                    {"ad": "Sazlıdere Barajı", "oran": 62.3}
                ]
            },
            # Diğer şehirler...
        ]

class AirQualityDataProvider(DataProvider):
    def get_data(self):
        # Hava kalitesi verilerini döndür
        pass

class DataProviderFactory:
    @staticmethod
    def create_provider(provider_type: str) -> DataProvider:
        if provider_type == "water":
            return WaterDataProvider()
        elif provider_type == "air":
            return AirQualityDataProvider()
        raise ValueError(f"Geçersiz provider tipi: {provider_type}") 