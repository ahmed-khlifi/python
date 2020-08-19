#very basic and simple just for study purposes
from bs4 import *
import requests

usr = input('username : ')
URL = "https://www.instagram.com/{}/"
rq = requests.get(URL.format(usr))
soup = BeautifulSoup(rq.text, "html.parser")
for l in soup.find_all('meta', {'property':'og:description'}):
    print(l['content'].split('-',1)[0])

#output : X Followers, X Following, X Posts 