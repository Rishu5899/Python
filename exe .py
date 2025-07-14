class Tution:
  def __init__(self,Name,Fees):
     self.Name = Name
     self.Fees = Fees
  def get_yearly(self):
     self.yearly=self.Fees * 12
     print(self.yearly)
s = Tution("Rishu",500)
s.get_yearly()
s.Fees = 800
s.get_yearly()
