import tweepy
from textblob import TextBlob
import os
from dotenv import load_dotenv
import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2.service_account import Credentials

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

# Set the search query parameters
query = 'Tacla Duran'
max_tweets = 100
since_id = None
until_id = None
lang = 'pt'

# Search for tweets containing the query
public_tweets = tweepy.Cursor(api.search_tweets, q=query, since_id=since_id, until_id=until_id, lang=lang).items(max_tweets)

# Perform sentiment analysis on each tweet
sentiments = []
tweets = []
for tweet in public_tweets:
    text = tweet.text
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    sentiments.append(sentiment)
    tweets.append(text)
    print(text)

# Create a DataFrame from the list of sentiments and tweets
data = {'Sentiment': sentiments, 'Tweet': tweets}
sentiments_data = pd.DataFrame(data)

# Authenticate with Google Cloud and create a BigQuery client
credentials = Credentials.from_service_account_file('config/gcp_credentials.json')

# Set the project ID and dataset ID
project_id = 'tech-tests-381614'
dataset_id = 'sentiments_twitter'

# Create the dataset if it does not exist
client = bigquery.Client(credentials=credentials, project=project_id)
dataset_ref = client.dataset(dataset_id)
try:
    dataset = client.get_dataset(dataset_ref)
    print('Dataset {} already exists.'.format(dataset_id))
except Exception as e:
    dataset = client.create_dataset(dataset_ref)
    print('Created dataset: {}'.format(dataset_id))

# Set the BigQuery table ID to store the sentiments
table_id = '{}.{}'.format(dataset_id, 'sentiments')

# Write the DataFrame to a BigQuery table
pandas_gbq.to_gbq(sentiments_data, table_id, project_id=project_id, if_exists='replace', credentials=credentials, table_schema=[{'name': 'Sentiment', 'type': 'FLOAT'}, {'name': 'Tweet', 'type': 'STRING'}])
