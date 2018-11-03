import twitterscraper
from threading import Thread
import time
import json
import datetime as dt


text=["@BetoORourke", "@tedcruz"]

def callTweets(text):
    u = twitterscraper.query_tweets(text, begindate=dt.date(2018,6,1))
    response = []
    for i in u:
        response.append({'user': str(i.user), 'age' : str(i.timestamp), 'tweet' : str(i.text)})
    with open(text[1:]+'.json', 'w') as f:
        res = json.dump(response, f, sort_keys=True, indent=4)
        #print(i.user)

threads = []
for keys in text:
    t = Thread(target=callTweets, args=(keys,))
    threads.append(t)
    t.start()
    time.sleep(.2)
