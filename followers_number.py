#very basic and simple just for study purposes
from bs4 import *
import requests
import sqlite3

def w(info):
    with open("info.txt", "w") as fw:
        fw.write(info)
check = 'script run for the first time'
try :
	with open("info.txt", "r") as fr:
	    check = fr.read()
except FileNotFoundError:
	pass
	
#change user name
usr = "khelifi_ahmed_"
URL = "https://www.instagram.com/{}/"
rq = requests.get(URL.format(usr))
soup = BeautifulSoup(rq.text, "html.parser")
for l in soup.find_all('meta', {'property':'og:description'}):
    info = l['content'].split('-',1)[0]
    w(info)

if check != info:
    print(f''' 
status updated :
old : {check}
new : {info}
    ''')
    w(info)
else:
    print("nothing changed")

#output : X Followers, X Following, X Posts 