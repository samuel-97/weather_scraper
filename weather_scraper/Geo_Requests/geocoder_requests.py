import requests

BASE_CALL_geocoder = "http://api.openweathermap.org/geo/1.0/direct?q="
LOCATION = ['Bakersfield,CA,USA', 'New York City,NY,USA', 'Amissville,VA,USA', 'Medellin,ANT,CO']
API_KEY = "e7e12faba846cdc8ec5dedaa05d09698"

request_bin = {}


for q in LOCATION:
    url = BASE_CALL_geocoder + q + "&limit=2" + "&appid=" + API_KEY
    request_bin[q] = requests.get(url).json()

print(request_bin)