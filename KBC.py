#KBC Game
Questions = [["Which language was used to create Facebook?","Python","Java","C++","HTML",4],
["Which language was used to create Whatsapp?","Python","Java","C++","HTML",],
["Which language was used to create Instagram?","Python","Java","C++","HTML",],
["Which language was used to create Snapchat?","Python","Java","C++","HTML",],
["Which language was used to create Gmail?","Python","Java","C++","HTML",],
]
levels = [1000,3000,6000,12000,24000]
money = 0
for i in range(0,len(Questions)):
    Question  = Questions[i]
    print(f"Question no 1 is for {levels[0]}")
    print( f"{Question[i]}")
    print(f"a.{Question[1]}        b.{Question[2]}")
    print(f"c.{Question[3]}        d.{Question[4]}")
    answer = int(input("Enter your Option "))
    if (answer == Question[-1]):
        print(f"Your answer is correct you won {levels[i]}")
        if(i==1):
         money += 1000
       
print(f"Total Price:{money}")


     
 


    # print(f"Question no 2 is for {levels[1]}")
    # print( f"{Question[0]}")
    # print(f"a.{Question[1]}        b.{Question[2]}")
    # print(f"c.{Question[3]}        d.{Question[4]}")
    # ans = str(input("Enter your Option "))
    # if ans == Question[2]:
    #     print(f"Your answer is correct you won {levels[1]}")
    #     if money (i == 1):
    #        money == 3000
    # else:
    #     print("Your answer is wrong")
    #     break

    