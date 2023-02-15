###### LIBRARIES ######
import tweepy
import pandas as pd
###### LIBRARIES ######

__author__ = 'Jorge Tarancon Rey'

class Twitter_Processor:
    def __init__(self,config):
        # Read required credentials
        self.api_key = config.get('TWITTER','API_KEY')
        self.api_secret_key = config.get('TWITTER','API_SECRET_KEY')
        self.access_token = config.get('TWITTER','ACCESS_TOKEN')
        self.access_token_secret = config.get('TWITTER','ACCESS_TOKEN_SECRET')
        self.bearer_token = config.get('TWITTER','BEARER_TOKEN')

    def creating_twitter_api(self):
        # Initializing client
        self.client = tweepy.Client(
                                bearer_token = self.bearer_token,
                                consumer_key = self.api_key,
                                consumer_secret = self.api_secret_key,
                                access_token = self.access_token,
                                access_token_secret = self.access_token_secret,
                                return_type = dict)
        
    def extract_tweets(self) -> dict:
        return self.client.get_users_tweets(
                                            id=self.client.get_user(username='elonmusk')['data']['id'],
                                            max_results=20)
        #return self.client.get_home_timeline(max_results=2)

    def cast_tweets_to_dataframe(self,tweets:dict) -> pd.DataFrame:
        return pd.DataFrame.from_dict(data=tweets['data'],orient='columns',columns=None)
        