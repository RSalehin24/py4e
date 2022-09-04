import urllib.request
import json

url = input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

json_data = json.loads(data)
comments = json_data["comments"]
sum_count = 0

print("Count:", len(comments))

for comment in comments :
  sum_count += comment["count"]

print(sum_count)
