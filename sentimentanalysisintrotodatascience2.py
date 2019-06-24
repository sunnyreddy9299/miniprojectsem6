from textblob import TextBlob
w=TextBlob("Angel is one of the worst song ever")
w.words
w.tags
print("polarity of textblob:")
print(w.sentiment.polarity)
import tweepy
consumer_key='v2TMZGC2Aa7nZJB8uJzoBHLAm'
consumer_secret='UJGgI8h0anzfOScrIVc1YwmFyQb8dHzF56Sl929es1br0tpFEt'
access_token='1017792924858318848-WXtk10vF0A4Bxt5p549GBZ4Q8Xlf1V'
access_token_secret='9oIbqhQocBH5ThOo47IqUnpMt8SydkWOEWEDAZO3t67NK'
#accessing tweets using tweepy.Oauthhandler
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('My hero academia')
for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment.polarity)