from bs4 import BeautifulSoup
import requests
lang = ['en', 'ru']
name = ['Cat', 'Кот']
for i in range(2):
    wikiUrl = f'https://{lang[i]}.wikipedia.org/wiki/{name[i]}'
    print(wikiUrl)
    soup = BeautifulSoup(requests.get(wikiUrl).content, 'lxml')
    for tag in soup.find_all("img", 'mw-file-element'):
        if '.jpg' in tag.get('src') or '.JPG' in tag.get('src'):
            print(tag.get('src'))