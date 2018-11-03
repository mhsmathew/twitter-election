__author__ = 'DavidW'
import twitterscraper

u = twitterscraper.query_tweets("mocosnow",10)
for i in u:
    print(i.user)