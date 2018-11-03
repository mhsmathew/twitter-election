import json
import datetime as dt
from datetime import timedelta
from datetime import datetime

files=["BetoORourke", "tedcruz"]
data=[]
for file in files:
    with open(file+'.json') as f:
        data.append(json.load(f))
time=[]
count1=[]
count2=[]
for single_date in (dt.date(2018,6,1) + timedelta(n) for n in range(30)):
    time.append(single_date)
    count=sum([1 for i in data[0] if str(datetime.strptime(i["age"], "%Y-%m-%d %H:%M:%S").date()) == str(single_date)])
    count1.append(count)
    count2.append(sum([1 for i in data[1] if str(datetime.strptime(i["age"], "%Y-%m-%d %H:%M:%S").date()) == str(single_date)]))
    #print(single_date)

for i in range(len(time)):
    print("Date: "+ str(time[i]) +" Democrats: "+ str(count1[i]) +" Republicans: " + str(count2[i]))
    

