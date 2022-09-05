class AnimalParty:
  member = 0
  
  def __init__(self):
    print("One object of 'AnimalParty' class is being constructed")  
  
  def member_count(self):
    self.member += 1
    print(self.member)
    
  def __del__(self):
    print("One object of AnimalParty is being deleted after counting", self.member, "members")

animal01 = AnimalParty()

# calling the object methoud
animal01.member_count()
animal01.member_count()

animal01 = 43

# Printing type and dir
# print()
# print("Type:", type(animal01))
# print()
# print("Methods and Data:")
# for each in dir(animal01):
#   print(each)

# dir and type of a string object
print()
string_object = str()
print("Type", type(string_object))
print()
print("Methods and data:")
for each in dir(string_object):
  print(each)
