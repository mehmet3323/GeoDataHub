class EventManager:
    _observers = {}

    @classmethod
    def subscribe(cls, event_type: str, callback):
        if event_type not in cls._observers:
            cls._observers[event_type] = []
        cls._observers[event_type].append(callback)

    @classmethod
    def unsubscribe(cls, event_type: str, callback):
        if event_type in cls._observers:
            cls._observers[event_type].remove(callback)

    @classmethod
    def notify(cls, event_type: str, data):
        if event_type in cls._observers:
            for callback in cls._observers[event_type]:
                callback(data) 