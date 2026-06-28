"""

https://catalog.api.2gis.com/3.0/items/geocode?
    q=Москва, Садовническая, 25 & 
    fields=items.point & 
    key=YOUR_KEY

"""

""
{'meta': {'api_version': '3.0.20835', 'code': 200, 'issue_date': '20260626'}, 
 'result':
     {'items':
       [
        {'address_name': 'Садовническая улица, 25', 
         'full_name': 'Москва, Садовническая улица, 25', 
         'id': '4504235282713264', 
         'name': 'Садовническая улица, 25', 
         'point': {'lat': 55.746397, 'lon': 37.634369}, 
         'purpose_name': 'Жилой дом', 'type': 'building'}
       ], 
     'total': 1}}
""


import requests

class API():
    def __init__(self, key): # передать параметром ключ
        self.key = key

    def get_coordinates(self, address):  # передавать сюда адрес
        payload = {
            'q': address,               
            'fields': 'items.point',                        
            'key': self.key                                 
        }

        r = requests.get('https://catalog.api.2gis.com/3.0/items/geocode', params= payload)
       
        data = r.json()
       
        lat = data['result']['items'][0]['point']['lat']
        lon = data['result']['items'][0]['point']['lon']
        return (lat, lon)
