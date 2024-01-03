
# Making Greeting Text Simulator


import time
Name = input("Tell Me Your Name: ")
hours = int(time.strftime("%H"))

if(hours >=4 and hours <12):
    print("Good Morning,",Name)
    print("Have a nice day!")
elif(hours >=12 and hours < 16):
    print("Good Afternoon,",Name)
    print("Have a nice noon!")
elif(hours >=16 and hours< 19):
    print("Good Evening,",Name)
    print("Have a nice evening!")
else:
    print("Good Night,",Name)
    print("Have a beautiful night!")



