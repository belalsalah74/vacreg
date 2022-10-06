import json
import pathlib
cities = pathlib.Path('vac/cities.json')

CITY_CHOICES = []
with open(cities) as file:
    data = json.load(file)[2].get('data')
    CITY_CHOICES = [(city.get('id'), city.get('city_name_en'))
                    for city in data if city.get("governorate_id") == '1']

