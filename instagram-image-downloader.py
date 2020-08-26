import urllib.request
from bs4 import BeautifulSoup
import random
from sys import argv
import os

if len(argv) != 2:
        print(f"usage : {argv[0]} picture_link")
        os._exit(1)
name = random.randrange(1, 50) # will change [TODO]


print('[/] just wait ..')
try:
    source_code = urllib.request.urlopen(argv[1])  # url
    soup = BeautifulSoup(source_code, "html.parser")  # get source code
    for link in soup.find_all('meta', {'property': 'og:image'}):  # find image url
        content = link.get('content')
        full_name = str(name) + '.jpg' #save the downloaded file
        urllib.request.urlretrieve(content, full_name)
        print('[+] saved as ' + full_name) # image saved in the directory of the script .
except urllib.request.HTTPError:
    print('error ') 

