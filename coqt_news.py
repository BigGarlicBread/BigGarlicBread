import requests
import json


url_temp = "https://newsapi.org/v2/everything?q=coronavirus&apiKey=65e83cc03d304f0db39ce33220f88e6f"

payload = {}
headers= {}

response = requests.request("GET", url_temp, headers=headers, data = payload)

data = response.text.encode('utf8')
js = json.loads(data)

def request_covid_news_title_description():
    news_title_descp = []

    for i in range (10):
        news_title_descp.append(js['articles'][i]['title'])
        news_title_descp.append(js['articles'][i]['description'])

    return news_title_descp

def request_covid_news_url():
    news_url = []

    for i in range (10):
        news_url.append(js['articles'][i]['url'])

    return news_url
