from cgitb import html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter the url: ')

# handle https
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Get the data and prepare beautiful soup
file_handler = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(file_handler, 'html.parser')

# retrieve the anchor tags
a_tags = soup('a')
for a_tag in a_tags:
  print(a_tag.get('href', None))
