import requests, re, json, random
from HTMLParser import HTMLParser
class webmethods():
    def pugme(self):
        url = 'http://www.pugbomb.me/'
        r = requests.get(url)
        xml = r.content
        result = re.search('<img src="(.+?)">', xml).group(0).split('"')[1]
        return result

    def catme(self):
        url = 'http://thecatapi.com/api/images/get?format=html'
        r = requests.get(url)
        xml = r.content
        # print xml
        result = re.search('<img src="(.+?)">', xml).group(1)
        return result

    def gifme(self, search):
        api_key = '&api_key=dc6zaTOxFJmzC'
        url = 'http://api.giphy.com/v1/gifs/search?q=' + search + api_key
        r = requests.get(url)
        r = r.content
        r = json.loads(r)
        r = [elem['url'] for elem in r['data']]
        return random.choice(r)

    def quoteme(self):
        with open('quotes.txt', 'r') as f:
            lst = f.readlines()
        f.close()
        return random.choice(lst)

test = webmethods()
test.quoteme()