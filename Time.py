import time
t = time.strftime("%H:%M:%S:")
hour = int(time.strftime("%H"))
hour = int(input("Enter hour : "))

if(hour >= 0 and hour <12):
    print("Good Morning")

elif(hour >= 12 and hour <17):
    print("Good Afternoon")

else:
    print("Good Night")