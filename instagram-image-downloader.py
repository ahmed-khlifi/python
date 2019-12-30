import urllib.request
from bs4 import BeautifulSoup
import random

url = input('The URL > ')  # default is downloading an image ..
name = random.randrange(1, 50) # give a random name to saved image 

def download():
    print('[/] just wait ..')
    try:
        source_code = urllib.request.urlopen(url)  # url
        soup = BeautifulSoup(source_code, "html.parser")  # get source code
        for link in soup.find_all('meta', {'property': 'og:image'}):  # find image url
            content = link.get('content')
            full_name = str(name) + '.jpg' #save the downloaded file
            urllib.request.urlretrieve(content, full_name)
            print('[+] saved as ' + full_name) # image saved in the directory of the script .
    except urllib.request.HTTPError:
        print('Public Accounts only or private ones you have access to them') #work on public accounts or privat if u following it
        
download()
