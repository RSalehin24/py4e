import urllib.request, urllib.parse
import json
import ssl

service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

#Ignore https ssl certificates
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

location = input("Enter your location: ")
params = dict()
params['address'] = location
params['key'] = 42
url = service_url + urllib.parse.urlencode(params)

print("Retrieving", url)
data = urllib.request.urlopen(url, context=context).read().decode()
print("Retrieved", len(data), "characters")

try :
  json_data = json.loads(data)
except :
  json_data = None
  
print("Location:", json.dumps(json_data, indent=4))
  
if not json_data or "status" not in json_data or json_data["status"] != "OK" :
  print("==== Failed to retrieve data ====")
  print(data)
else :
  print("Retrieved Data:")
  print(data)
