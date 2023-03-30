from geopy.geocoders import Nominatim
import requests

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my-application-name contact@example.com")

# Get the latitude and longitude of a city
location = geolocator.geocode("Contagem, Brazil")
lat, lon = location.latitude, location.longitude

# Use the Yahoo! Where On Earth ID API to get the WOEID of the city
url = f"https://www.yahoo.com/news/_tdnews/api/resource/WeatherSearch;text={lat},{lon}"
response = requests.get(url)
woeid = response.json()["weatherSearch"]["results"][0]["woeid"]

print(f"Contagem WOEID: {woeid}")