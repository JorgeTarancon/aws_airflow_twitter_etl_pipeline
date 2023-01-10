###### LIBRARIES ######
import configparser
import tweepy
from processors import twitter_processor
###### LIBRARIES ######

###### CONFIG ######
config = configparser.ConfigParser()
config.read('config.ini')
###### CONFIG ######


# Initiate Twitter Processor with personal credentials
tp = twitter_processor.Twitter_Processor(config=config)

# Create an API object
tp.creating_twitter_api()

# Extracting Tweets
tweets = tp.extract_tweets()

# Converting the tweets in a pandas DataFrame
tweets_df = tp.cast_tweets_to_dataframe(tweets=tweets)
print(tweets_df)