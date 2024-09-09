import requests
import json

query = input('Enter the topic you are looking to read about: ')
url = f'https://newsapi.org/v2/top-headlines?q={query}&country=in&apiKey=044ad189fe6545daaf1e4f7ee6d059ad'
r = requests.get(url)
news = json.loads(r.text)
i = 1
for article in news["articles"]:
    if i<6:
        print(article['title'])
        print(article['description'],"\n\n")
        i = i+1
    else:
        break
