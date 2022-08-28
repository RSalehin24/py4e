from asyncio import constants
import urllib.request
from bs4 import BeautifulSoup
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
data = urllib.request.urlopen(url, context = context).read()
soup = BeautifulSoup(data, 'html.parser')
spans = soup('span')

total = 0

for span in spans:
  total += int(span.contents[0])
  
print(total)
