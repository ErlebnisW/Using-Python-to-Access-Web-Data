from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')
print('Retrieving:',url)

count = int(count)
position = int(position) - 1
for i in range(count):
    urls = list()
    html = urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    for tag in tags:
        urls.append(tag.get('href', None))
    url = urls[position]
    print('Retrieving:',url)
    