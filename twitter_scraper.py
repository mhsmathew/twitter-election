from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import datetime
from threading import Thread
import write
import json

races=[]

with open('races.json') as f:
    races.append(json.load(f))
write.setup()

def link(dia, handle):
    return getCount("https://twitter.com/search?f=tweets&vertical=default&q=to%3A" + handle + "%20since%3A" + str(dia) + "%20until%3A" + str(dia + datetime.timedelta(days= 1)) + "&src=typd&lang=en")

def getCount(link):
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    a=[]
    b=[]
    time.sleep(3)
    b = browser.find_elements_by_class_name("stream-item");
    while len(a)!=len(b):
        b = browser.find_elements_by_class_name("stream-item");
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.7)
        a = browser.find_elements_by_class_name("stream-item");
    browser.quit()
    return(len(a))
count1=[]
count2=[]

def run(user, state, party):
    for i in range(0, (datetime.date.today() - datetime.date(2018, 6,1)).days, 7):
        if party=='D':
            count1.append(link(datetime.date(2018, 6, 1) + datetime.timedelta(days = i), user))
            print(state,":", party,": ", count1[-1])
        if party=='R':
            count2.append(link(datetime.date(2018, 6, 1) + datetime.timedelta(days = i), user))
            print(state,":",party,": ", count2[-1])
print(races[0][0])
for race in races[0][::-1]:
    count1=[]
    count2=[]
    t = Thread(target=run, args=(race['Democrat'], race['State'],'D',))
    c = Thread(target=run, args=(race['Republican'], race['State'],'R'))
    c.start()
    t.start()
    c.join()
    t.join()
    write.addOn(race['State'], count1, count2)


