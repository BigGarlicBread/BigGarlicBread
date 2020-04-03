import os
import json
import requests
import matplotlib.pyplot as plt
import datetime as dt

user_code = input('Enter the first country code: ')

url = "https://thevirustracker.com/free-api?countryTimeline="+user_code

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

data = response.text.encode('utf8')
js = json.loads(data)

totalcases = []
dates = []
for i in js['timelineitems'][0].keys():
    if i == 'stat':
        break

    totalcase = js['timelineitems'][0][i]['total_cases']
    totalcases.append(totalcase)
    dates.append(i)

plt.plot(dates, totalcases)
plt.title('Graph of total cases in country code: ' + user_code)
plt.xlabel('Dates --->')
plt.ylabel('Cases --->')
plt.show()
