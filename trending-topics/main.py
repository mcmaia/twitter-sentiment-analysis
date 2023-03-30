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

brazil_trends = api.get_place_trends(23424768) #Brazil
belo_horizonte_trends = api.get_place_trends(455821) #BH
rj_trends = api.get_place_trends(455821) #rj


print("###Trending topics in Brazil###:")
for trend in brazil_trends[0]["trends"]:
    print(trend["name"])

print("###Trending topics in Belo Horizonte:###")
for trend in belo_horizonte_trends[0]["trends"]:
    print(trend["name"])
    
print("####Trending topics in RJ###:")
for trend in rj_trends[0]["trends"]:
    print(trend["name"])
