import os as os

# Import tweepy to work with the twitter API
import tweepy as tw

# Import pandas to work with dataframes
import pandas as pd

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from matplotlib import pyplot as plt
# Import seaborn
import seaborn as sns



access_token = "265883877-GpCqj1v5xmldPwth8gxfzzXFB8jrCWMkLTV7sZzA"
access_token_secret ="aJccQubnObHbnTLhjDvxTn4MpOd2m5ejpeJQAofgEAPAR"
consumer_key ="Mr9PbqVDHi4kDvlI1cBEKrzAZ"
consumer_secret="G2xjFPyiKOpa8gdAPUQQ3oQ57fO2tht97qayDjAKXHkhG94lOY"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
# Set Tokens
auth.set_access_token(access_token, access_token_secret)
# Instantiate API
api = tw.API(auth, wait_on_rate_limit=True)


handle = 'taylorswift13'

res = api.user_timeline(screen_name=handle, count=100, include_rts=True)
tweets = [tweet.text for tweet in res]
tweets
text = ''.join(str(tweet) for tweet in tweets)


authenticator = IAMAuthenticator('wEm2-sAb_vWL4M1EK0Tp6n6SVynCqoGCC01usqHamsU5')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/48093617-cf08-42dd-8a3b-09de4fd5cd27')

response = natural_language_understanding.analyze(
    text = text,
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=1))).get_result()

print(json.dumps(response, indent=2))
