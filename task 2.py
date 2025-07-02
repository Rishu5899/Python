# Cafe Alaska
print("Enter 1 for Vadapav Order")
print("Enter 2 for Dabeli Order")
print("Enter 3 for Burger Order")
print("Enter 4 for MaskaBun Order")
print("Enter 5 for Puff Order")
print("Enter 6 for Soda Order")
print("Enter 7 for Water Order")
print("Enter 8 for Chai Order")

da=(input("Enter your Order : "))


match da:
    case 1:
     vadapav = int(input("Enter your Quantity"))
     if( vadapav < 3):
      print(vadapav  * 30)
     if (vadapav >= 3):
      print(vadapav  * 30 - 18.00)

    case 2:
     Dabeli = int(input("Enter your Quantity"))
     if( Dabeli < 3):
      print(Dabeli  * 40)
     if (Dabeli >= 3):
      print(Dabeli  * 40 - 24.00)

    case 3:
     Burger = int(input("Enter your Quantity"))
     if( Burger < 3):
      print(Burger  * 50)
     if (Burger >= 3):
      print(Burger  * 50 - 30.00)
    
    case 4:
     MaskaBun = int(input("Enter your Quantity"))
     if( MaskaBun < 3):
      print(MaskaBun  * 30)
     if (MaskaBun >= 3):
      print(MaskaBun  * 30 - 18.00)
      
    case 5:
     Puff = int(input("Enter your Quantity"))
     if( Puff < 3):
      print(Puff  * 45)
     if (Puff >= 3):
      print(Puff  * 45 - 27.00)
          
    case 6:
     Soda = int(input("Enter your Quantity"))
     if( Soda < 3):
      print(Soda  * 20)
     if (Soda >= 3):
      print(Soda  * 20 - 12.00) 

    case 7:
     Water = int(input("Enter your Quantity"))
     if( Water < 3):
      print(Water  * 10)
     if (Water >= 3):
      print(Water  * 10 - 6.00) 

    case 8:
     Chai = int(input("Enter your Quantity"))
     if( Chai < 3):
      print(Chai  * 12)
     if (Chai >= 3):
      print(Chai  * 30 - 18.00)        
       