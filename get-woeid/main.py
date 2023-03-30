import tweepy
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate Twitter API credentials
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create a Tweepy API object
api = tweepy.API(auth)

# Get the trending topics for a specific location
trends = api.available_trends()

brazil_woeid = None
belo_horizonte_woeid = None
rio_de_janeiro_woeid = None
contagem_woeid = None

for location in trends:
    if 'Brazil' in location['name']:
        brazil_woeid = location['woeid']
    if 'Belo Horizonte' in location['name']:
        belo_horizonte_woeid = location['woeid']
    if 'Rio de Janeiro' in location['name']:
        rio_de_janeiro_woeid = location['woeid']
    if 'Contagem' in location['name']:
        contagem_woeid = location['woeid']

if brazil_woeid:
    print(f"Brazil WOEID: {brazil_woeid}")
else:
    print("Brazil not found")

if belo_horizonte_woeid:
    print(f"Belo Horizonte WOEID: {belo_horizonte_woeid}")
else:
    print("Belo Horizonte not found")

if rio_de_janeiro_woeid:
    print(f"RJ WOEID: {rio_de_janeiro_woeid}")
else:
    print("RJ not found")

if contagem_woeid:
    print(f"Contagem WOEID: {contagem_woeid}")
else:
    print("Contagem not found")