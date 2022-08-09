import streamlit as st
from tweepy import API,OAuthHandler
from textblob import TextBlob

api_key = 'kjnuVeyEy4yOk4KUFoDx0Jf3J'
api_secret = 'g1fVqAZYBdU9EN9fazzLFrcOsmJ6P5lfOeqImWKCjYC8KAWVPE'

st.title("Twitter Sentimental Analysis")
authentication=OAuthHandler(api_key,api_secret)
twitter_api=API(authentication)

def clean(tweet):
    tweet_words=str(tweet).split(" ")
    tweet_words=[word for word in tweet_words if not word.startswith('#')]
    return ' '.join(tweet_words)


text=st.text_input("enter text: ")
if st.button("predict"):
    tweets=twitter_api.search_tweets(text,count=5)
    #st.write(tweets)
    #list comprehension
    
    cleaned_tweets=[clean(tweet.text) for tweet in tweets]
    for tweet in cleaned_tweets:
        tweet_polarity=TextBlob(tweet).sentiment.polarity
        if tweet_polarity<0:
            st.error(tweet+" -> Negative tweet")
        else:
            st.success(tweet+" -> Positive tweet")