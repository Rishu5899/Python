# # Cafe Alaska
# print("Enter 1 for Vadapav Order")
# print("Enter 2 for Dabeli Order")
# print("Enter 3 for Burger Order")
# print("Enter 4 for MaskaBun Order")
# print("Enter 5 for Puff Order")
# print("Enter 6 for Soda Order")
# print("Enter 7 for Water Order")
# print("Enter 8 for Chai Order")

# da=(input("Enter your Order : "))



# vadapav = int(input("Enter your Quantity"))
# if( vadapav < 3):
#       print(vadapav  * 30)
# if (vadapav >= 3):
#       print(vadapav  * 30 - 18.00)

    
# Dabeli = int(input("Enter your Quantity"))
# if( Dabeli < 3):
#       print(Dabeli  * 40)
# if (Dabeli >= 3):
#       print(Dabeli  * 40 - 24.00)


# Burger = int(input("Enter your Quantity"))
# if( Burger < 3):
#       print(Burger  * 50)
# if (Burger >= 3):
#       print(Burger  * 50 - 30.00)
    

# MaskaBun = int(input("Enter your Quantity"))
# if( MaskaBun < 3):
#       print(MaskaBun  * 30)
# if (MaskaBun >= 3):
#       print(MaskaBun  * 30 - 18.00)
      

# Puff = int(input("Enter your Quantity"))
# if( Puff < 3):
#       print(Puff  * 45)
# if (Puff >= 3):
#       print(Puff  * 45 - 27.00)
          
   
# Soda = int(input("Enter your Quantity"))
# if( Soda < 3):
#       print(Soda  * 20)
# if (Soda >= 3):
#       print(Soda  * 20 - 12.00) 

    
# Water = int(input("Enter your Quantity"))
# if( Water < 3):
#       print(Water  * 10)
# if (Water >= 3):
#       print(Water  * 10 - 6.00) 

# Chai = int(input("Enter your Quantity"))
# if( Chai < 3):
#       print(Chai  * 12)
# if (Chai >= 3):
#       print(Chai  * 30 - 18.00)        
       
menu = {
    "1": ("Vadapav", 30),
    "2": ("Dabeli", 40),
    "3": ("Burger", 50),
    "4": ("MaskaBun", 30),
    "5": ("Puff", 45),
    "6": ("Soda", 20),
    "7": ("Water", 10),
    "8": ("Chai", 12)
}

total = 0

# Let user add 3 items
for i in range(3):
    item_no = input(f"\nEnter item number {i+1} (1-8): ")
    
    if item_no not in menu:
        print("Invalid item. Try again.")
        continue

    item_name, price = menu[item_no]
    qty = int(input(f"Enter quantity of {item_name}: "))

    # Apply discount if qty >= 3
    if qty >= 3:
        discount = price * qty * 0.20  # 20% discount
    else:
        discount = 0

    item_total = price * qty - discount
    total += item_total

    print(f"{item_name} x {qty} = ₹{item_total:.2f} (Discount: ₹{discount:.2f})")

print(f"\nTotal bill = ₹{total:.2f}")