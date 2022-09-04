import json

data = '''
{
  "name" : "Reyan",
  "phone" : {
    "type" : "intl",
    "number" : "+8801608537383"
  },
  "email" : {
    "hide" : "yes"
  }
}
'''

info_thyself = json.loads(data)

print('Name:', info_thyself['name'])
print('Phone:', info_thyself['phone']['number'])
print('Hide email:', info_thyself['email']['hide'])

data_01 = '''
[
  {
    "id" : "001",
    "x" : "02",
    "name" : "Reyan"
  },
  {
    "id" : "002",
    "x" : "04",
    "name" : "Salehin"
  }
]
'''

print()

users = json.loads(data_01)
print("User count:", len(users))

for user in users:
  print("id:", user["id"])
  print("x:", user["x"])
  print("Name:", user["name"])
  print()
