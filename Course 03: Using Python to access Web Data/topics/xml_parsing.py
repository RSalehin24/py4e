import xml.etree.ElementTree as element_tree 

data = '''
<person>
  <name>Reyan</name>
  <age>21</age>
  <phone type="intl">+8801608537383</phone>
  <email hide="yes"/>
</person>
'''

tree = element_tree.fromstring(data)

print('Name: ', tree.find('name').text)
print('Phone: ', tree.find('phone').text)
print('Email hide attribute: ', tree.find('email').get('hide'))

print('\n')

data0 = '''
<staff>
  <users>
    <user x='01'>
      <id>01</id>
      <name>Reyan</name>
    </user>
    <user x='02'>
      <id>02</id>
      <name>Yeasir</name>
    </user>
  </users>
</staff>
'''

staff = element_tree.fromstring(data0)
list_staff = staff.findall('users/user')

print('Total users: ', len(list_staff))
print()

for user in list_staff:
  print('id: ', user.find('id').text)
  print('Name: ', user.find('name').text)
  print('Attribute: ', user.get('x'))
  print()
