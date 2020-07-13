from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
print('Retrieving:',url)
data = urlopen(url,context=ctx).read()

info = json.loads(data)
print('Retrieving',len(info['comments']),'characters')

sum = 0
counts = 0
for item in info['comments']:
   sum = sum + item['count']
   counts = counts + 1

print('Count:',counts)
print('Sum:',sum)