# Example of Encapsulation 

class Car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cut = False

    def start(self):
        self.acc = True
        self.brk = True
        print("Car started")
w = Car()
w.start()