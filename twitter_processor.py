###### LIBRARIES ######
import tweepy
import pandas as pd
import configparser
###### LIBRARIES ######

__author__ = 'Jorge Tarancon Rey'

class TwitterProcessor:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Read required credentials
        self.api_key = config.get('TWITTER','API_KEY')
        self.api_secret_key = config.get('TWITTER','API_SECRET_KEY')
        self.access_token = config.get('TWITTER','ACCESS_TOKEN')
        self.access_token_secret = config.get('TWITTER','ACCESS_TOKEN_SECRET')
        self.bearer_token = config.get('TWITTER','BEARER_TOKEN')

    def creating_twitter_client(self):
        # Initializing client
        self.client = tweepy.Client(
                                bearer_token = self.bearer_token,
                                consumer_key = self.api_key,
                                consumer_secret = self.api_secret_key,
                                access_token = self.access_token,
                                access_token_secret = self.access_token_secret,
                                return_type = dict)
    
    def creating_twitter_api(self):
        # Initializing API
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        
    def extract_tweets_by_user(self, username:str='elonmusk', max_results:int=20) -> dict:
        return self.client.get_users_tweets(
                                            id=self.client.get_user(username=username)['data']['id'],
                                            max_results=max_results)

    def extract_tweets_by_keyword(self, keyword:str='Ukraine', max_results:int=20) -> dict:
        #return self.api.search_tweets(q=keyword, count=max_results, lang='en', result_type='recent')
        return self.client.search_all_tweets(
                                            query=keyword,
                                            max_results=max_results,
                                            lang='en',
                                            result_type='recent')

    def cast_tweets_to_dataframe(self,tweets:dict) -> pd.DataFrame:
        return pd.DataFrame.from_dict(data=tweets['data'],orient='columns',columns=None)

    def run_twitter_etl(self):
        self.creating_twitter_client()

        tweets = self.extract_tweets_by_keyword(keyword='Ukraine')

        tweets_df = self.cast_tweets_to_dataframe(tweets)
        
        #tweets_df.to_csv(path_or_buf='s3://bucket-twitter/tweets.csv', sep=';', index=False, ecndoing='latin-1')
        print(tweets_df)