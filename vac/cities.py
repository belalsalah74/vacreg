import json

with open(r'vac\cities.json') as file:
    data = json.load(file)

CITY_CHOICES = [[city.get('id'), city.get('city_name_en')] for city in data]
