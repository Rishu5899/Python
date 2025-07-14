class Student:
 def __init__(self,Name,Fees):
  self.Name=Name
  self.Fees=Fees

 def get_avg(self):
  self.Fees * 12
  print(self.Fees)

s1 = Student("Rishu",500)
s1.get_avg()