# Get User Input
while True:
    try:
        C = float(input("Enter the Celsius: "))
        break
# Only accepts int
    except:
        print("Please input a float.")

F = C * (9 / 5) + 32
print(F)