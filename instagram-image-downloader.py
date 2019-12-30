import urllib.request
from bs4 import BeautifulSoup
import random

url = input('The URL > ')  # default is downloading an image ..
name = random.randrange(1, 50)


def download():
    print('[/] just wait ..')
    try:
        source_code = urllib.request.urlopen(url)  # get the source code
        soup = BeautifulSoup(source_code, "html.parser")  # get source code
        for link in soup.find_all('meta', {'property': 'og:image'}):  # get the url
            content = link.get('content')
            full_name = str(name) + '.jpg'
            urllib.request.urlretrieve(content, full_name)
            print('[+] saved as ' + full_name)
    except urllib.request.HTTPError:
        print('Public Accounts only')


download()
