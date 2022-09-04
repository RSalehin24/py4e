from multiprocessing import context
import ssl
import urllib.request, urllib.parse
import xml.etree.ElementTree as element_tree

# Ignore ssl certificate for https
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
url = address
print('Retrieving', url)
data = urllib.request.urlopen(url, context=context).read()

print('Retrieved', len(data), 'characters')

data = data.decode()
tree = element_tree.fromstring(data)
counts = tree.findall('comments/comment/count')
print('Count:', len(counts))

sum_count = 0
for count in counts:
  sum_count += int(count.text)

print('Sum:', sum_count)
