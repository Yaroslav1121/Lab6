from bs4 import BeautifulSoup
import requests
from collections import Counter
r = requests.get("https://www.bbc.com/news/health-59378849")
page = BeautifulSoup(r.text, 'html.parser')

print(r.status_code)
ryadok1 = page.head.title.text
ryadok2 = page.body.text
text = ryadok2.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace('"', "").replace("-", "")
text = text.replace("  ", " ")
text = text.lower()
words1 = text.split(" ")

Counter = Counter(words1)
for word in []:
        Counter[word] += 1

print(Counter)
input()
