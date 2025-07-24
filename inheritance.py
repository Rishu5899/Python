
# Single Inheritance
class car:
    def start(self):
     print("Start")

    def stop(self):
       print("Stop")

class toyota(car):
       print("Fortuner") 

# Multi-level Inheritance
class Fortuner(toyota):
    def __init__(self,type):
        self.type = type

sq = Fortuner("Diesel")
print(sq.type,sq.start(),sq.stop())
