#very basic and simple just for study purposes
from bs4 import *
import requests

rq = requests.get("https://www.instagram.com/khelifi_ahmed_/")
soup = BeautifulSoup(rq.text, "html.parser")
for l in soup.find_all('meta', {'property':'og:description'}):
    print(l['content'].split('-',1)[0])