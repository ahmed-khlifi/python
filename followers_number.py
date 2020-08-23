#very basic and simple just for study purposes
from bs4 import *
import requests
import sqlite3

def w(info):
    with open("info.txt", "w") as fw:
        fw.writelines(info)

try :
	with open("info.txt", "r") as fr:
	    check = fr.read()
except FileNotFoundError:
	check = 'script run for the first time'
	
#change user name
usr = "khelifi_ahmed_"
URL = "https://www.instagram.com/{}/"

print("listening for changes ..")
while True:
	rq = requests.get(URL.format(usr))
	soup = BeautifulSoup(rq.text, "html.parser")
	for l in soup.find_all('meta', {'property':'og:description'}):
		info = l['content'].split('-',1)[0]
		if check != info:
			print(f"status updated :\n old : {check}\n new : {info} ")
			w(info)
			break


#output : X Followers, X Following, X Posts 
