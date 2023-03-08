###### LIBRARIES ######
import tweepy
import pandas as pd
import configparser
###### LIBRARIES ######

__author__ = 'Jorge Tarancon Rey'

def creating_twitter_api():
    # Read required credentials
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config.get('TWITTER','API_KEY')
    api_secret_key = config.get('TWITTER','API_SECRET_KEY')
    access_token = config.get('TWITTER','ACCESS_TOKEN')
    access_token_secret = config.get('TWITTER','ACCESS_TOKEN_SECRET')
    bearer_token = config.get('TWITTER','BEARER_TOKEN')

    # Initializing client
    client = tweepy.Client(
                            bearer_token = bearer_token,
                            consumer_key = api_key,
                            consumer_secret = api_secret_key,
                            access_token = access_token,
                            access_token_secret = access_token_secret,
                            return_type = dict)
    
    return client

def extract_tweets(client):
    return client.get_users_tweets(
                                    id=client.get_user(username='elonmusk')['data']['id'],
                                    max_results=20)
    #return self.client.get_home_timeline(max_results=2)

def cast_tweets_to_dataframe(tweets:dict) -> pd.DataFrame:
    return pd.DataFrame.from_dict(data=tweets['data'],orient='columns',columns=None)

def run_twitter_etl():

    client = creating_twitter_api()

    tweets = extract_tweets(client)

    tweets_df = cast_tweets_to_dataframe(tweets)
    
    tweets_df.to_csv(path_or_buf='s3://bucket-twitter/tweets.csv', sep=';', index=False, encoding='latin-1')