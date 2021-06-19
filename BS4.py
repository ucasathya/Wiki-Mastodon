import requests
from bs4 import BeautifulSoup
i=input("Enter Input:")
url=f"https://ta.wiktionary.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%B1%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AF%81:Search?search={i}&fulltext=%E0%AE%A4%E0%AF%87%E0%AE%9F%E0%AF%81%E0%AE%95&ns0=1"
page = requests.get(url=url)
soup = BeautifulSoup(page.content, 'html.parser')
cricket_score = soup.find('div',class_="searchresult").text
print(cricket_score)
