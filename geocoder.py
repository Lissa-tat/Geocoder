from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="fhgjgjkg")
# location = geolocator.geocode("175 5th Avenue NYC")
# print(location.address)
# # Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
# print((location.latitude, location.longitude))
# # (40.7410861, -73.9896297241625)
# print(location.raw)
# # {'place_id': '9167009604', 'type': 'attraction', ...}


class Geocoder():
    def __init__(self):
        # self.address = "1600 Amphitheatre Parkway, Mountain View, CA"
        self.address = "Novosibirsk"
    
        self.geolocator = Nominatim(user_agent="qwerty")
        self.location: tuple[float, float]

    def location(self):  
        # Вызываем метод geocode объекта геокодера для геокодирования адреса
        self.location = self.geolocator.geocode(self.address)
 
        # Печатаем результат
        print("Адрес:", self.address)
        print("Широта:", self.location.latitude)
        print("Долгота:", self.location.longitude)

        return self.location.latitude, self.location.longitude