import datetime
import random, json, csv

#Sets up .csv. Only do this once
def setup():
    with open("tweets.csv","w") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["State","Date","Democrat","Republican"])

#This appends it. Start with first state alphabetically. 
def addOn(state, demArray, repArray):
    with open("tweets.csv","a") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(demArray)):
            writer.writerow([state, str(datetime.date(2018, 6, 1) + datetime.timedelta(days = 7*i)), demArray[i], repArray[i]])
