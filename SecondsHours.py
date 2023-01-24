# Get User Input
while True:
    try:
        x = int(input("Enter the Seconds: "))
        break
# Only accepts int
    except:
        print("Please input a int.")

hours = x // (60*60) # division by 3600 sec
minutes = (x // 60) - (hours * 60) # divison by 60 sec minus the minutes in each hour
seconds = x - ((hours * 3600) + (minutes * 60)) # seconds in each hour and in each minutes minus starting sec

# Output
print(hours, "hours,", minutes, "minutes, and", seconds, "seconds")