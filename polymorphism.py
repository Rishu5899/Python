class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def se(self):
        print(self.real,"p +", + self.img,"hy")

    def addo(self,num2):
         
        return complex(self.img  + num2)
    
sw = complex(45,57)
print(sw.addo())