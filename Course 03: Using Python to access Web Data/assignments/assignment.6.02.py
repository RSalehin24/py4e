import urllib.request, urllib.parse
import json

service_url = "http://py4e-data.dr-chuck.net/json?"
location = input("Enter location: ")
params = dict()
params['address'] = location
params['key'] = 42
url = service_url + urllib.parse.urlencode(params)

print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

json_data = json.loads(data)
print("Place id",json_data["results"][0]["place_id"])

