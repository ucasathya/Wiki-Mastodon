import requests
from bs4 import BeautifulSoup
from mastodon import Mastodon
import random
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
i=random.choice(words)
url=f"https://ta.wiktionary.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%B1%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AF%81:Search?search={i}&fulltext=%E0%AE%A4%E0%AF%87%E0%AE%9F%E0%AF%81%E0%AE%95&ns0=1"
page = requests.get(url=url)
soup = BeautifulSoup(page.content, 'html.parser')
c = soup.find('div',class_="searchresult").text
mastodon = Mastodon(
    
                access_token = 'spxq-ji5UCJ3GCUEvFjart739K6tttG5dlQGog9D7h0',
                api_base_url = 'https://mastodon.social'
            )
mastodon.status_post(str(c))
print("sucess")
