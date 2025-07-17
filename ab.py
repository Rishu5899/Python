class Dat:
    def __init__(self,name):
     self.name = name
    
    @staticmethod
    def hello():
       print("hello")

e = Dat("Rishu")
print(e.name)
e.hello()