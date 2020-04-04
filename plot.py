import os
import json
import requests
import matplotlib.pyplot as plt
import datetime as dt

user_code = input('Enter the country code: ')

url = "https://thevirustracker.com/free-api?countryTimeline="+user_code

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

data = response.text.encode('utf8')
js = json.loads(data)

totalcases = []
dailycases = []
totaldeaths = []
totalrecovery = []
dates = []

for i in js['timelineitems'][0].keys():
    if i == 'stat':
        break

    totalcases.append(js['timelineitems'][0][i]['total_cases'])
    dailycases.append(js['timelineitems'][0][i]['new_daily_cases'])
    totaldeaths.append(js['timelineitems'][0][i]['total_deaths'])
    totalrecovery.append(js['timelineitems'][0][i]['total_recoveries'])
    dates.append(i)

plt.figure('Total Cases')
plt.plot(dates, totalcases)
plt.title('Graph of total cases in country code: ' + user_code)
plt.xlabel('Dates --->')
plt.ylabel('Cases --->')

plt.figure('Daily Cases')
plt.bar(dates, dailycases)
plt.title('Graph of daily cases in country code: ' + user_code)
plt.xlabel('Dates --->')
plt.ylabel('Cases --->')

plt.figure('Total Deaths')
plt.plot(dates, totaldeaths)
plt.title('Graph of total deaths in country code: ' + user_code)
plt.xlabel('Dates --->')
plt.ylabel('Deaths --->')

plt.figure('Total Recovery')
plt.plot(dates[:-2], totalrecovery[:-2])
plt.title('Graph of total recovery in country code: ' + user_code)
plt.xlabel('Dates --->')
plt.ylabel('Recoveries --->')

plt.show()
