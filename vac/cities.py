import json
CITY_CHOICES = []
with open(r'vac\cities.json') as file:
    data = json.load(file)[2].get('data')
    CITY_CHOICES = [(city.get('id'), city.get('city_name_en'))
                    for city in data if city.get("governorate_id") == '1']

