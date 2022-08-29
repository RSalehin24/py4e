from turtle import position
import urllib.request
import ssl
from bs4 import BeautifulSoup

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print('Retrieving:', url)

for i in range(count):
  temp_position = position
  html_data = urllib.request.urlopen(url, context = context).read()
  soup = BeautifulSoup(html_data, 'html.parser')
  anchor_tags = soup('a')

  for anchor_tag in anchor_tags:
    temp_position -= 1
    if temp_position == 0:
      url = anchor_tag.get('href', None)
  
  print('Retrieving:', url)
