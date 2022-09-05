class DungeonParty:
  member_count = 0
  
  def __init__(self, member):
    self.member_count = member
    print("A Dungeon Party being built")
    
  def adding_members(self, member):
    self.member_count += member

class BirdsDungeonParty(DungeonParty):
  points = 0
  balance = 0
  
  def killing_bird_monster(self):
    self.points += 100
    
  def point_conversion(self):
    self.balance = round(self.points*0.857)

reyansparty = BirdsDungeonParty(5)
print("Initial member count:", reyansparty.member_count)
reyansparty.killing_bird_monster()
reyansparty.point_conversion()
print("Balance after killing 01 monster bird:", reyansparty.balance)
reyansparty.adding_members(4)
print("Member count after adding 04 more members:", reyansparty.member_count)
